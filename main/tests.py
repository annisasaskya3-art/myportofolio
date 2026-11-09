from django.contrib.auth.models import Group, User
from django.test import TestCase, Client
from django.urls import reverse

from main.models import Project, Experience

class MainTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title="Future Fest Presentation as The Speaker",
            description="Merancang modul pelatihan dan presentasi interaktif.",
            tech_stack="Presentation Design",
            project_url=""
        )

    def test_main_url_is_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_experience_url_is_exist(self):
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)

    def test_projects_url_is_exist(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)

    def test_projects_content_display(self):
        # Halaman Projects sudah AJAX: data datang dari endpoint JSON.
        response = self.client.get('/api/projects/')
        self.assertContains(response, 'Future Fest Presentation as The Speaker')

class ExperienceAjaxTest(TestCase):
    """Tugas 5: AJAX list, search, tambah via POST, hak akses, XSS."""

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)
        self.superuser = User.objects.create_superuser("owner", password="pw12345!")
        self.editor = User.objects.create_user("editor", password="pw12345!")
        self.editor.groups.add(Group.objects.create(name="Editor"))
        self.visitor = User.objects.create_user("visitor", password="pw12345!")
        self.exp = Experience.objects.create(
            title="Vice Project Officer at SIWAK-NG 2026",
            description="Led technical operations.",
            category="volunteer",
        )
        self.payload = {
            "title": "Research Assistant",
            "description": "Membantu riset.",
            "category": "research",
            "thumbnail": "",
        }

    # --- halaman & JSON ---
    def test_page_is_skeleton_only(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "SIWAK-NG 2026")  # data baru dimuat lewat AJAX
        self.assertContains(response, 'id="experience-grid"')

    def test_json_readable_by_anonymous_with_star_info(self):
        self.exp.stars.add(self.visitor)
        data = self.client.get(reverse("main:get_experience_json")).json()
        item = data["results"][0]
        self.assertEqual(item["title"], "Vice Project Officer at SIWAK-NG 2026")
        self.assertEqual(item["stars_count"], 1)
        self.assertFalse(item["is_starred"])
        self.assertFalse(item["can_edit"])

    def test_json_is_starred_for_logged_in_user(self):
        self.exp.stars.add(self.visitor)
        self.client.login(username="visitor", password="pw12345!")
        item = self.client.get(reverse("main:get_experience_json")).json()["results"][0]
        self.assertTrue(item["is_starred"])

    def test_search_filters_by_title(self):
        Experience.objects.create(title="Teaching Assistant", description="x", category="part-time")
        url = reverse("main:get_experience_json")
        titles = [r["title"] for r in self.client.get(url, {"q": "siwak"}).json()["results"]]
        self.assertEqual(titles, ["Vice Project Officer at SIWAK-NG 2026"])
        self.assertEqual(self.client.get(url, {"q": "tidak-ada"}).json()["count"], 0)

    # --- POST tambah data ---
    def test_anonymous_cannot_add(self):
        response = self.client.post(reverse("main:create_experience_ajax"), self.payload)
        self.assertEqual(response.status_code, 403)

    def test_visitor_cannot_add(self):
        self.client.login(username="visitor", password="pw12345!")
        response = self.client.post(reverse("main:create_experience_ajax"), self.payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

    def test_superuser_can_add(self):
        self.client.login(username="owner", password="pw12345!")
        response = self.client.post(reverse("main:create_experience_ajax"), self.payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Experience.objects.count(), 2)

    def test_editor_cannot_add(self):
        self.client.login(username="editor", password="pw12345!")
        response = self.client.post(reverse("main:create_experience_ajax"), self.payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

    def test_invalid_input_returns_400_with_errors(self):
        self.client.login(username="owner", password="pw12345!")
        response = self.client.post(reverse("main:create_experience_ajax"), {**self.payload, "title": ""})
        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])

    def test_get_not_allowed_on_add(self):
        self.client.login(username="owner", password="pw12345!")
        self.assertEqual(self.client.get(reverse("main:create_experience_ajax")).status_code, 405)

    def test_csrf_is_enforced(self):
        strict = Client(enforce_csrf_checks=True)
        strict.login(username="owner", password="pw12345!")
        response = strict.post(reverse("main:create_experience_ajax"), self.payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

    # --- XSS ---
    def test_html_only_input_is_rejected(self):
        self.client.login(username="owner", password="pw12345!")
        evil = "<img src=\"x\" onerror=\"alert('XSS!')\">"
        response = self.client.post(reverse("main:create_experience_ajax"), {**self.payload, "title": evil})
        self.assertEqual(response.status_code, 400)

    def test_tags_are_stripped_from_text(self):
        self.client.login(username="owner", password="pw12345!")
        response = self.client.post(
            reverse("main:create_experience_ajax"),
            {**self.payload, "title": "Intern <script>alert(1)</script>"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertNotIn("<", Experience.objects.get(pk=response.json()["id"]).title)

    # --- star & hapus ---
    def test_toggle_star_requires_login(self):
        url = reverse("main:toggle_star_experience", args=[self.exp.id])
        self.assertEqual(self.client.post(url).status_code, 401)
        self.client.login(username="visitor", password="pw12345!")
        self.assertEqual(self.client.post(url).json(), {"is_starred": True, "stars_count": 1})
        self.assertEqual(self.client.post(url).json(), {"is_starred": False, "stars_count": 0})

    def test_delete_only_superuser(self):
        url = reverse("main:delete_experience_ajax", args=[self.exp.id])
        self.client.login(username="editor", password="pw12345!")
        self.assertEqual(self.client.post(url).status_code, 403)
        self.client.login(username="owner", password="pw12345!")
        self.assertEqual(self.client.post(url).status_code, 200)
        self.assertEqual(Experience.objects.count(), 0)
