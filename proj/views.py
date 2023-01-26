from django.shortcuts import render
from proj.models import Proj

# Create your views here.

def project_index(request):
    projs = Proj.objects.all()
    context = {
        "projs": projs
    }
    return render(request, "project_index.html", context)

def proj_detail(request, pk):
    proj = Proj.objects.get(pk=pk)
    context = {
        "proj": proj
    }
    return render(request, "proj_detail.html", context)

