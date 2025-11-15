from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def resume_view(request):
    return render(request, "resume.html")

def writing_samples_view(request):
    return render(request, "writing_samples.html")

def losp_view(request):
    return render(request, "losp.html")
