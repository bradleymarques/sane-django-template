from django.urls import path

from pages.views import HomeView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
]
