from rest_framework import permissions

class IsTaskListAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return True
        return False
        
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        return request.user.profile == obj.created_by
    
class IsTaskAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return  request.user.profile.house != None
        return False
        
    def has_object_permission(self, request, view, obj):
        
        return request.user.profile == obj.task_list.house
    
class IsAttachmentAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return  request.user.profile.house != None
        return False
        
    def has_object_permission(self, request, view, obj):
        
        return request.user.profile == obj.task.task_list.house
