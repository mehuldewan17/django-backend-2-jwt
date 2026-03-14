from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import food_view, signup

urlpatterns = [
    path("signup/", signup),
    path("login/", TokenObtainPairView.as_view()),
    path("food/", food_view),
]