from django.urls import path
from .views import RegistrationView, LoginView


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('signin', LoginView.as_view()),
]
