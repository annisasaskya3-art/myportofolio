import uuid
from django.contrib.auth.models import Group, User
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Project, Experience


class ProjectAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner",
            password="test-password",
            email="owner@example.com",
        )
        self.visitor = User.objects.create_user(
            username="visitor",
            password="test-password",
        )
        self.project = Project.objects.create(
            title="Portfolio",
            description="My website",
            tech_stack="Django",
        )

        self.list_url = reverse("api:project-list")
        self.detail_url = reverse(
            "api:project-detail", args=[self.project.id]
        )
        self.star_url = reverse(
            "api:project-star", args=[self.project.id]
        )

        self.payload = {
            "title": "New project",
            "description": "A useful app",
            "tech_stack": "Python",
            "project_url": "https://example.com/",
            "project_image_url": "",
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], self.project.id)
        self.assertFalse(response.data[0]["is_starred"])
        self.assertEqual(
            self.client.get(self.detail_url).status_code,
            status.HTTP_200_OK,
        )

    def test_search_and_empty_results(self):
        response = self.client.get(self.list_url, {"title": "PORT"})
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            self.list_url, {"title": "not-found"}
        )
        self.assertEqual(response.data, [])

    def test_missing_project(self):
        url = reverse("api:project-detail", args=[999999])
        self.assertEqual(
            self.client.get(url).status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)

            self.assertEqual(
                self.client.post(
                    self.list_url, self.payload, format="json"
                ).status_code,
                status.HTTP_403_FORBIDDEN,
            )
            self.assertEqual(
                self.client.patch(
                    self.detail_url,
                    {"title": "Changed"},
                    format="json",
                ).status_code,
                status.HTTP_403_FORBIDDEN,
            )
            self.assertEqual(
                self.client.delete(self.detail_url).status_code,
                status.HTTP_403_FORBIDDEN,
            )

        self.assertEqual(Project.objects.count(), 1)

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(
            self.list_url, self.payload, format="json"
        )
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)

        for changes, field in [
            ({"title": "   "}, "title"),
            (
                {"title": '<img src="x" onerror="alert(1)">'},
                "title",
            ),
            ({"project_url": "javascript:alert(1)"}, "project_url"),
        ]:
            response = self.client.post(
                self.list_url,
                {**self.payload, **changes},
                format="json",
            )
            self.assertEqual(
                response.status_code, status.HTTP_400_BAD_REQUEST
            )
            self.assertIn(field, response.data)

        self.assertEqual(Project.objects.count(), 1)

    def test_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.patch(
            self.detail_url, {"title": "Changed"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.project.refresh_from_db()
        self.assertEqual(self.project.description, "My website")

        response = self.client.put(
            self.detail_url, {"title": "Incomplete"}, format="json"
        )
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )

        response = self.client.put(
            self.detail_url, self.payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(self.detail_url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(response.content, b"")

    def test_star_requires_login_and_toggles(self):
        response = self.client.post(self.star_url)
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

        self.client.force_authenticate(user=self.visitor)

        response = self.client.post(self.star_url)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)

        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            {
                **self.payload,
                "star_count": 99,
                "is_starred": True,
                "starred_by_names": "forged",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_staff_cannot_manage_tutorial_projects(self):
        self.visitor.is_staff = True
        self.visitor.save()

        self.client.force_authenticate(user=self.visitor)
        response = self.client.patch(
            self.detail_url,
            {"title": "Changed"},
            format="json",
        )
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.delete(self.list_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def test_session_write_without_csrf_is_rejected(self):
        from rest_framework.test import APIClient

        client = APIClient(enforce_csrf_checks=True)
        client.login(username="owner", password="test-password")

        response = client.post(
            self.list_url, self.payload, format="json"
        )
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_session_write_with_csrf_succeeds(self):
        from rest_framework.test import APIClient

        client = APIClient(enforce_csrf_checks=True)
        client.login(username="owner", password="test-password")

        page = client.get(
            self.list_url, HTTP_ACCEPT="text/html"
        )
        self.assertEqual(page.status_code, status.HTTP_200_OK)

        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url,
            self.payload,
            format="json",
            HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

class ExperienceAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(username="owner_exp", email="o@example.com", password="pw12345!")
        self.editor = User.objects.create_user(username="editor_exp", password="pw12345!")
        self.editor.groups.add(Group.objects.create(name="Editor"))
        self.member = User.objects.create_user(username="member_exp", password="pw12345!")
        self.exp = Experience.objects.create(title="Research Assistant", description="Membantu riset.", category="research")
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse("api:experience-detail", args=[self.exp.id])
        self.star_url = reverse("api:experience-star", args=[self.exp.id])
        self.payload = {"title": "Volunteer", "description": "Mengajar.", "category": "volunteer", "thumbnail": ""}

    def assert_db_untouched(self):
        self.exp.refresh_from_db()
        self.assertEqual(self.exp.title, "Research Assistant")
        self.assertEqual(Experience.objects.count(), 1)

    def test_public_can_read_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], str(self.exp.id))
        self.assertFalse(response.data[0]["is_starred"])
        self.assertEqual(self.client.get(self.detail_url).status_code, 200)

    def test_missing_experience_returns_404(self):
        url = reverse("api:experience-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_guest_and_member_cannot_write(self):
        for user in (None, self.member):
            self.client.force_authenticate(user=user)
            for method, url, data in [
                ("post", self.list_url, self.payload),
                ("put", self.detail_url, self.payload),
                ("patch", self.detail_url, {"title": "Hacked"}),
                ("delete", self.detail_url, None),
            ]:
                response = getattr(self.client, method)(url, data, format="json")
                self.assertEqual(response.status_code, 403, f"{method} oleh {user}")
        self.assert_db_untouched()

    def test_editor_can_patch_and_put_but_not_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)
        response = self.client.patch(self.detail_url, {"title": "Diubah Editor"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.exp.refresh_from_db()
        self.assertEqual(self.exp.title, "Diubah Editor")
        self.assertEqual(self.exp.description, "Membantu riset.")  # PATCH hanya mengubah field yang dikirim
        self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 200)

        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)
        self.assertTrue(Experience.objects.filter(pk=self.exp.pk).exists())

    def test_owner_can_create_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Experience.objects.count(), 2)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Experience.objects.filter(pk=self.exp.pk).exists())

    def test_search_by_title_or_category(self):
        Experience.objects.create(title="Magang Backend", description="x", category="internship")
        response = self.client.get(self.list_url, {"q": "RESEARCH"})
        self.assertEqual([i["title"] for i in response.data], ["Research Assistant"])
        self.assertEqual(len(self.client.get(self.list_url, {"q": "internship"}).data), 1)
        self.assertEqual(self.client.get(self.list_url, {"q": "tidak-ada"}).data, [])
