from django.utils.html import strip_tags
from rest_framework import serializers
from main.permissions import is_editor
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
    category_label = serializers.CharField(source = "get_category_display", read_only = True)
    is_ongoing = serializers.BooleanField(read_only = True)
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category", "category_label", 
            "thumbnail", "stared_at", "ended_at", "is_ongoing", 
            "star_count", "is_starred", "can_edit", "can_delete",
        ]
        read_only_field = ["id", "stared_at"]

    @staticmethod
    def _clean_text(value, label):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(f"{label} tidak boleh kosong atau hanya berisi tag HTML.")
        return value

    def validate_title(self, value):
        return self._clean_text(value, "Judul")

    def validate_description(self, value):
        return self._clean_text(value, "Deskripsi")

    def get_star_count(self, obj):
        return len(obj.stars.all())

    def get_is_starred(self, obj):
        user = getattr(self.context.get("request"), "user", None)
        if user is None or not user.is_authenticated:
            return False
        return any (u.pk == user.pk for u in obj.stars.all())

    def _permissions(self):
        """(can_edit, can_delete) untuk request ini, dihitung sekali per serializer."""
        if not hasattr(self, "_cached_permissions"):
            user = getattr(self.context.get("request"), "user", None)
            if user is None or not user.is_authenticated:
                self._cached_permissions = (False, False)
            else:
                self._cached_permissions = (user.is_superuser or is_editor(user), user.is_superuser)
        return self._cached_permissions

    def get_can_edit(self, obj):
        return self._permissions()[0]

    def get_can_delete(self, obj):
        return self._permissions()[1]