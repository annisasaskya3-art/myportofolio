from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from main.models import Experience

class MainTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.experience = Experience.objects.create(
            title="Pembicara di Future Fest 2026",
            description="Berbagi wawasan dan memandu ratusan siswa SMA.",
            category="volunteer",
        )

    def test_main_url_is_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_nonexistent_page(self):
        response = self.client.get('/halaman-yang-tidak-ada/')
        self.assertEqual(response.status_code, 404)

    def test_experience_model_creation(self):
        self.assertEqual(self.experience.title, "Pembicara di Future Fest 2026")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page_renders_model_data(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experience.html')
        self.assertContains(response, "Pembicara di Future Fest 2026")
        self.assertContains(response, "Volunteer")

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))
        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")