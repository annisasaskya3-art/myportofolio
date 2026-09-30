from django.urls import path
from main.views import (
    show_main,
    show_experience,
    create_experience,
    edit_experience,
    delete_experience,
    show_json_experience,
    show_projects,
    create_project,
    get_projects_json,
    edit_project,
    delete_project,
    register,
    login_user,
    logout_user,
    toggle_star,
    show_xml,
    show_json,
    show_xml_by_id,
    show_json_by_id,
    add_project_ajax,
    create_project_ajax,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),

    # --- EXPERIENCE URLS (primary key UUID) ---
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/edit/<uuid:id>/", edit_experience, name="edit_experience"),
    path("experience/delete/<uuid:id>/", delete_experience, name="delete_experience"),
    path("experience/json/", show_json_experience, name="show_json_experience"),

    # --- PROJECT URLS ---
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/edit/<int:project_id>/", edit_project, name="edit_project"),
    path("projects/delete/<int:project_id>/", delete_project, name="delete_project"),
    path("projects/<int:project_id>/star/", toggle_star, name="toggle_star"),
    path("api/projects/", get_projects_json, name="get_projects_json"),

    # --- DATA DELIVERY URLS ---
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<str:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<str:id>/", show_json_by_id, name="show_json_by_id"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),


    # --- AUTH ---
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]