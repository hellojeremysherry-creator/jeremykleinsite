from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def resume_view(request):
    return render(request, "resume.html")

def writing_samples_view(request):
    return render(request, "writing_samples.html")

def losp_view(request):
    return render(request, "losp.html")

def packet_view(request):
    """Page that contains the full LOSP materials packet / buttons."""
    return render(request, "packet.html")

def appellate_brief_view(request):
    """Writing sample: Appellate brief focused on the Pregnancy Discrimination Act."""
    return render(request, "appellate_brief.html")  # 👈 NEW

def memo_of_law_view(request):
    """Writing sample: Appellate brief focused on the Pregnancy Discrimination Act."""
    return render(request, "memo_of_law.html")  # 👈 NEW

def materials_view(request):
    """Hub page for résumé + writing samples."""
    return render(request, "materials.html")

# NEW LOSP doc pages

def losp_overview_view(request):
    """Standalone page for the LOSP Overview One-Pager."""
    return render(request, "losp_overview.html")

def losp_studyplan_view(request):
    """Standalone page for the LOSP Year 1 Study Plan."""
    return render(request, "losp_studyplan.html")

def losp_schedule_tth_view(request):
    """Standalone page for the Tues/Thurs weekly schedule."""
    return render(request, "losp_schedule_tth.html")

def losp_schedule_weekend_view(request):
    """Standalone page for the weekend-integrated weekly schedule."""
    return render(request, "losp_schedule_weekend.html")

# LOSP forms detail pages (Section A)

def admission_status_view(request):
    """Standalone page for the Admission Status Page."""
    return render(request, "admission_status.html")

def admission_confirmation_letter(request):
    """Standalone page for the Approval Letter Page."""
    return render(request, "admission_confirmation.html")

# LOSP forms detail pages (Section C)

def losp_notice_intent_view(request):
    """Standalone page for the LOSP Notice of Intent form."""
    return render(request, "losp_notice_intent.html")

def losp_supervisor_decl_view(request):
    """Standalone page for the Supervising Attorney / Judge Declaration."""
    return render(request, "losp_supervisor_decl.html")

def losp_semi_cover_view(request):
    """Standalone page for the Semiannual Report Cover Sheet."""
    return render(request, "losp_semi_cover.html")

def losp_semi_detail_view(request):
    """Standalone page for the Semiannual Report Detail Form."""
    return render(request, "losp_semi_detail.html")

# Legal authority detail pages (Section D)

def losp_rules_title4_view(request):
    """Standalone page for Rules of the State Bar, Title 4, Division 1."""
    return render(request, "losp_rules_title4.html")

def losp_bpc_6060_view(request):
    """Standalone page for Business & Professions Code §§ 6060–6061."""
    return render(request, "losp_bpc_6060.html")

def losp_portal_defs_view(request):
    """Standalone page for State Bar Admissions Portal status definitions."""
    return render(request, "losp_portal_defs.html")