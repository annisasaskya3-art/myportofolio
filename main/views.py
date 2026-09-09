# Create your views here.

from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        "name": "Annisa Saskya Aulia", 
        "npm": "2506537915",           
        "study_program": "S1 Sistem Informasi", 
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Annisa Saskya Aulia", 
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)