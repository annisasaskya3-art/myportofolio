from django.test import TestCase, Client
from django.urls import reverse
from main.models import Project

class MainTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Buat data dummy yang cocok sama judul barumu
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
        response = self.client.get('/projects/')
        self.assertContains(response, 'Future Fest Presentation as The Speaker')

    def test_experience_content_display(self):
        # Buat data dummy experience
        from main.models import Experience
        Experience.objects.create(
            title="Vice Project Officer at SIWAK-NG 2026",
            description="Led technical operations.",
            category="Leadership"
        )
        response = self.client.get('/experience/')
        self.assertContains(response, 'SIWAK-NG 2026')