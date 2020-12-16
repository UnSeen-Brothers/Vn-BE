from django.urls import path
# from .views import UserView, SingleUserView, SignUp, ExamView, QuestionView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView
from .views import NotesView


urlpatterns = [
    path('notes/', NotesView.as_view({"get": "list", "post":"create"}), name="single-note"),
    path('notes/<int:pk>/', NotesView.as_view({"get": "retrieve", "post":"update"})),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]