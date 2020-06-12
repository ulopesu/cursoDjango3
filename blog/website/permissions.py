from rest_framework.permissions import permissions


class contatosPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.user.is_staff:
            return True
        return False


