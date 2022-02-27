from django.urls import path, include
from rest_framework.routers import DefaultRouter

from usermanagement.views import MoviesView, CustomUserView

moviesrouter = DefaultRouter()

moviesrouter.register(r"movies", MoviesView, basename="movies")
moviesrouter.register(r"customuser", CustomUserView, basename="customuser")

