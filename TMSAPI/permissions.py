from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff  # Managers have `is_staff=True`

class IsAssignee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assignee == request.user  # Users can modify their own tasks
