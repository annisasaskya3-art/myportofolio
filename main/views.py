# Create your views here.

from django.shortcuts import render
from main.models import Experience
from main.models import Project
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm
from django.core import serializers
from django.http import HttpResponse
from main.models import Project

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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import serializers
from main.models import Project


def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Annisa Saskya Aulia",  # Ubah sesuai nama kamu
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)  # Sesuaikan jika nama filemu projects.html

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Annisa Saskya Aulia",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_xml(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")