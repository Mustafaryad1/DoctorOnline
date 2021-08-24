from django.urls import path
from doctorApp.views import register, CustomAuthToken

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('register', register, name="register")
]