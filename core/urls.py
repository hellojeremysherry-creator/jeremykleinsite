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

# NEW: Section A — Official Registration & Status forms
    path("losp/reg-status/admission-status/", views.admission_status_view, name="admission_status"),
    path("losp/reg-status/admission-confirm/", views.admission_confirmation_letter, name="admission_confirmation_letter"),

# NEW: Section C — Official LOSP forms
    path("losp/forms/notice-intent/", views.losp_notice_intent_view, name="losp_notice_intent"),
    path("losp/forms/supervising-attorney/", views.losp_supervisor_decl_view, name="losp_supervisor_decl"),
    path("losp/forms/semiannual-cover/", views.losp_semi_cover_view, name="losp_semi_cover"),
    path("losp/forms/semiannual-detail/", views.losp_semi_detail_view, name="losp_semi_detail"),

    # NEW: Section D — Legal authority
    path("losp/rules/title4/", views.losp_rules_title4_view, name="losp_rules_title4"),
    path("losp/rules/bpc-6060/", views.losp_bpc_6060_view, name="losp_bpc_6060"),
    path("losp/portal-defs/", views.losp_portal_defs_view, name="losp_portal_defs"),
]

