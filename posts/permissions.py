from rest_framework import permissions

class update(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            if request.method == "POST":

                return False

            return True

        return obj.id == request.user.id