from rest_framework import permissions

class IsUserAuthenticatedOrReadOnly(permissions.BasePermission):
    '''
    custom permisssions for UserViewset
    '''
    def has_permission(self, request, view):
        return True # it is accled only get request and post request
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return request.user == obj
        
        return False
    

class IsProfileAuthenticatedOrReadOnly(permissions.BasePermission):
    '''
    custom permisssions for UserViewset
    '''
    def has_permission(self, request, view):
        return True # it is accled only get request and post request
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return request.user.profile == obj
        
        return False
