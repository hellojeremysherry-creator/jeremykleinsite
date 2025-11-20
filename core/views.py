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

def materials_view(request):
    """Hub page for résumé + writing samples."""
    return render(request, "materials.html")