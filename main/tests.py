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

class ExperiencePageTest(TestCase):
    """Halaman Experience hanya kerangka; datanya dimuat lewat fetch() ke /api/v1/."""

    def setUp(self):
        Experience.objects.create(
            title="Vice Project Officer at SIWAK-NG 2026",
            description="Led technical operations.",
            category="volunteer",
        )

    def test_page_is_skeleton_only(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "SIWAK-NG 2026")  # data baru dimuat lewat API
        self.assertContains(response, 'id="experience-grid"')
        self.assertContains(response, reverse("api:experience-list"))  # container menunjuk ke API