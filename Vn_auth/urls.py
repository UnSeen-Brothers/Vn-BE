from django.urls import path
# from .views import UserView, SingleUserView, SignUp, ExamView, QuestionView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]