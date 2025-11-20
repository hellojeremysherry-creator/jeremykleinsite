from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("packet/", views.packet_view, name="packet"),  # 👈 new page with the docs
    path("materials/", views.materials_view, name="materials"),
    path("resume/", views.resume_view, name="resume"),

    # (Optional: keep these for direct links or future redirects)
    path("writing-samples/", views.writing_samples_view, name="writing_samples"),
    path(
        "writing-samples/appellate-brief/",
        views.appellate_brief_view,
        name="appellate_brief",
    ),

    path("writing-samples/", views.writing_samples_view, name="writing_samples"),
    path("writing-samples/appellate-brief/", views.appellate_brief_view, name="appellate_brief"),  # 👈 NEW
    path("losp/", views.losp_view, name="losp"),
]
