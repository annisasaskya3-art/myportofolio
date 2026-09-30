import datetime

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied 
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.views.decorators.http import require_POST

from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm

import datetime

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Annisa Saskya Aulia",
        "npm": "2506537915",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan desain aplikasi dan spendidikan."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


# --- EXPERIENCE VIEWS ---

def show_experience(request):
    context = {
        "name": "Annisa Saskya Aulia",
        "experience_list": Experience.objects.order_by("-started_at"),
        "can_edit": request.user.is_superuser or is_editor(request.user),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not (request.user.is_superuser or is_editor(request.user)):
        return HttpResponseForbidden("403 Forbidden: Anda tidak memiliki akses.")
    
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Annisa Saskya Aulia",
        "form": form,
    }
    return render(request, "create_experience.html", context)

@login_required(login_url="/login/")
def edit_experience(request, id):
    if not (request.user.is_superuser or is_editor(request.user)):
        return HttpResponseForbidden("403 Forbidden: Anda tidak memiliki akses.")
    
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Annisa Saskya Aulia",
        "form": form,
    }
    return render(request, "edit_experience.html", context)

@login_required(login_url="/login/")
def delete_experience(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("403 Forbidden: Hanya Superuser yang dapat menghapus data.")
    
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    
    return redirect("main:show_experience")

def show_json_experience(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# --- PROJECT VIEWS ---


def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Annisa Saskya Aulia",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "projects.html", context)

@login_required(login_url="/login/") 
def create_project(request):
    # Cek apakah akun yang sedang login adalah superuser (admin/pemilik)
    # Kalau bukan, langsung hentikan dengan error 403 Forbidden
    if not request.user.is_superuser:
        return HttpResponseForbidden("403 Forbidden: Hanya pemilik portofolio yang dapat menambah data.")

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

@login_required(login_url= "/login/")
def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if not (request.user.is_superuser or is_editor(request.user)):
        return HttpResponseForbidden("403 Forbidden: Anda tidak memiliki akses untuk mengubah proyek.")

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name" : "Annisa Saskya Aulia",
        "form" : form,
        "project" : project,
    }

    return render(request, "projects_form.html", context)

@login_required(login_url="/login/") 
def delete_project(request, project_id):
    # Cek apakah pengguna adalah superuser
    if not request.user.is_superuser:
       return HttpResponseForbidden("403 Forbidden: Hanya pemilik portofolio yang dapat menghapus data.")
    
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

# --- AUTHENTICATION VIEWS ---

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Annisa Saskya Aulia",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Annisa Saskya Aulia",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# --- FEATURE & SERIALIZER VIEWS ---

@login_required(login_url="/login/")
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if project.stars.filter(pk=request.user.pk).exists():
        project.stars.remove(request.user)
    else:
        project.stars.add(request.user)

    return redirect("main:show_projects")

def is_editor(user):
    return user.is_authenticated and user.groups.filter(name = 'Editor').exists()

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
    query = request.GET.get('q', '').strip()
    projects = Project.objects.all().order_by('-pk')
    if query:
        projects = projects.filter(title__icontains=query)

    can_edit = request.user.is_superuser or is_editor(request.user)
    can_delete = request.user.is_superuser

    data = []
    for p in projects:
        data.append({
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'category': getattr(p, 'tech_stack', '') or 'Project',
            'project_url': getattr(p, 'project_url', '') or '',
            'image_url': p.image.url if getattr(p, 'image', None) else None,
            'stars_count': p.stars.count(),
            'is_starred': request.user.is_authenticated and p.stars.filter(pk=request.user.pk).exists(),
            'can_edit': can_edit,
            'can_delete': can_delete,
        })
    return JsonResponse(data, safe=False)

@login_required(login_url='/auth/login')
def add_project_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        tech_stack = request.POST.get('tech_stack')
        description = request.POST.get('description')
        project_url = request.POST.get('project_url', '')

        if title and description:
            new_project = Project(
                title=title,
                tech_stack=tech_stack, # Sesuaikan nama field pada model Project kamu
                description=description,
                project_url=project_url,
                user=request.user
            )
            new_project.save()

            return HttpResponse(b"CREATED", status=201)

    return HttpResponseBadRequest()

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)