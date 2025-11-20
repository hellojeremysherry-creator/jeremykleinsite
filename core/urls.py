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

    # NEW: individual LOSP doc pages
    path("losp/overview/", views.losp_overview_view, name="losp_overview"),
    path("losp/study-plan/", views.losp_studyplan_view, name="losp_studyplan"),
    path("losp/schedule/tues-thurs/", views.losp_schedule_tth_view, name="losp_schedule_tth"),
    path("losp/schedule/weekends/", views.losp_schedule_weekend_view, name="losp_schedule_weekend"),
]

