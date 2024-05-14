from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission): 
  

    def has_object_permission(self, request, view, obj):

        message='permission denied,your not be owner'

        if request.method in permissions.SAFE_METHODS:
            return True

      
        return obj.user == request.user
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user