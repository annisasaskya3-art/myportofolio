from django.core import serializers
from django.http import HttpResponse
from main.models import Project  # Sesuaikan dengan modelmu

# 1. Menampilkan seluruh data dalam format XML
def show_xml(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# 2. Menampilkan seluruh data dalam format JSON
def show_json(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# 3. Menampilkan data spesifik berdasarkan ID dalam format XML
def show_xml_by_id(request, id):
    data = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# 4. Menampilkan data spesifik berdasarkan ID dalam format JSON
def show_json_by_id(request, id):
    data = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")