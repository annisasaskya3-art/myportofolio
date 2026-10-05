from django import forms
from django.forms import ModelForm, Select, TextInput, Textarea, URLInput
from django.utils.html import strip_tags

from main.models import Project
from main.models import Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category", "thumbnail"]

    def clean_text(self, field_name):
        value = strip_tags(self.cleaned_data.get(field_name, "")).strip()
        if not value: 
            raise forms.ValidationError("Isi tidak boleh kosong atau hanya berisi tag HTML.")
        return value

    def clean_title(self):
        return self.clean_text("title")

    def clean_description(self):
        return self.clean_text("description")