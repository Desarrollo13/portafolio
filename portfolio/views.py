from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    # recupero datos 
    projects=Project.objects.all()
    return render(request,"portfolio/portfolio.html",{'projects':projects})

