from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change projects."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )

def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "Hanya pemilik portofolio atau Editor yang dapat mengubah data."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return request.method in ("PUT", "PATCH") and is_editor(request.user)