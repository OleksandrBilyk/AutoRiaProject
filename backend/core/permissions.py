from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsAuthenticatedForGetOrWriteOnly(BasePermission):
    def has_permission(self, request: Request, view):
        if request.method == 'POST':
            return True
        return request.user.is_active

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)
