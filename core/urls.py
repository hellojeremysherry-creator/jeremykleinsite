from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("resume/", views.resume_view, name="resume"),
    path("writing-samples/", views.writing_samples_view, name="writing_samples"),
    path("losp/", views.losp_view, name="losp"),
]
