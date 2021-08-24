from rest_framework import permissions
from .models import User


class IsProfileOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        return request.user == User.objects.get(pk=view.kwargs['pk'])


class IsDoctor(permissions.BasePermission):
    """
    Custom permission to allow only Doctors.
    """

    def has_permission(self, request, view):
        return request.user.user_type == 'doctor'


class IsPatient(permissions.BasePermission):
    """
    Custom permission to allow only Patients.
    """

    def has_permission(self, request, view):
        return request.user.user_type == 'patient'
