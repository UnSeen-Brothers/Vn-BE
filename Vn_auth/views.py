from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import Notes
from .serializers import NotesSerializer
from .permissions import IsNoteOwner
from rest_framework_simplejwt import authentication as jwt_auth


# Create your views here.

class NotesView(viewsets.ModelViewSet):
    '''
    list: User Notes List\n
    Returns a List of Notes created by the currently authenticated user

    retrieve: Retrieve a Note\n
    Retreives a Single Notes instance by the id parameter specified in the URL if Owned by the Authenticated User 

    update: Updates a Note Instance\n
    Updates a Single Notes instance by the id parameter specified in the URL

    create: Create A Note\n
    Creates a Notes instance with the request.data values.
    Note that this view Content-Type Header must be 'multipart/form-data'
    '''

    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    authentication_classes = [jwt_auth.JWTAuthentication]
    permission_classes = [IsNoteOwner]
    
    # def has_permissions(self, request):
    #     print("perms")
    #     permission_classes = []
    #     restricted_actions = ["partial_update", "destroy", "update", "retrieve"]

    #     if self.action in restricted_actions:
    #         permission_classes = [IsNoteOwner]

    #     return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        raise exceptions.PermissionDenied()
    