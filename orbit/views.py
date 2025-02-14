from django.shortcuts import render,redirect

from .models import About, Category, Portfolio, Service, Education, HappyClients, WorkExperience
from .forms import Contact, ContactForm


def index(request):
    about=About.objects.all()
    portfolio=Portfolio.objects.all()[::-1]
    category=Category.objects.all()
    service=Service.objects.all()
    education=Education.objects.all()
    happy=HappyClients.objects.all()
    work=WorkExperience.objects.all()
    contact=ContactForm(request.POST or None)
    if contact.is_valid():
        contact.save()
        return redirect("/")
    ctx={
        'about':about,
        'portfolios':portfolio,
        'category':category,
        'services':service,
        'education':education,
        'happy':happy,
        'work':work,
        'form':contact
    }
    return render(request,'index.html',ctx)