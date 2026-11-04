from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Project


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
            "can_edit", "can_delete",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        # Diubah dari starred_by menjadi stars sesuai models.py
        return obj.stars.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        # Diubah dari starred_by menjadi stars
        return request.user in obj.stars.all()

    def get_starred_by_names(self, obj):
        # Diubah dari starred_by menjadi stars
        return ", ".join(user.username for user in obj.stars.all())

    def get_can_edit(self, obj):
        request = self.context.get("request")
        return (
            request is not None
            and request.user.is_authenticated
            and request.user.is_superuser
        )

    def get_can_delete(self, obj):
        request = self.context.get("request")
        return (
            request is not None
            and request.user.is_authenticated
            and request.user.is_superuser
        )

class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category",
            "thumbnail", "started_at", "ended_at",
            "star_count", "is_starred",
        ]
        read_only_fields = ["id", "started_at", "star_count", "is_starred"]

    def get_star_count(self, obj):
        return obj.stars.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return obj.stars.filter(pk=request.user.pk).exists()