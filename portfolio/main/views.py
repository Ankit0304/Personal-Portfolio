from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    about = About.objects.all()
    education = Education.objects.all()
    skills = Skills.objects.all()
    experience = Experience.objects.all()
    projects = Projects.objects.all()
    contact = Contact.objects.all()
    link = Link.objects.all()
    
    context = {
        'about': about,
        'education': education,
        'skills': skills,
        'experience': experience,
        'projects': projects,
        'contact': contact,
        'link': link,
    }
    return render(request, 'index.html')
