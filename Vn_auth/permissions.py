from rest_framework import permissions


class IsNoteOwner(permissions.BasePermission):
# this is a custom permission to reatrict access to Update and Delete another users exam
    message = "User is not the Owner of this note"
    
    def has_permissions(self, request):

        restricted_actions = ["partial_update", "destroy", "update", "retrieve"]

        if self.action in restricted_actions:
            return obj.owner == request.user

        if self.action == "create":
            return request.user.is_authenticated

        return False