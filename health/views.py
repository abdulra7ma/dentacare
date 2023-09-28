from django import views
from django.shortcuts import render
from django.views import generic


def home(request):
    return render(request, "home.html", {})


class HomeView(generic.TemplateView):
    template_name = "home.html"
    


def contact(request):
    return render(request, "contact.html", {})
