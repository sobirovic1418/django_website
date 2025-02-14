from calendar import month

from django.shortcuts import render
from unicodedata import category

from .models import About, Category, Portfolio, Service, Education, HappyClients, WorkExperience


def index(request):
    about=About.objects.all()
    portfolio=Portfolio.objects.all()[::-1]
    category=Category.objects.all()
    service=Service.objects.all()
    education=Education.objects.all()
    happy=HappyClients.objects.all()
    work=WorkExperience.objects.all()
    ctx={
        'about':about,
        'portfolios':portfolio,
        'category':category,
        'services':service,
        'education':education,
        'happy':happy,
        'work':work,
    }
    return render(request,'index.html',ctx)