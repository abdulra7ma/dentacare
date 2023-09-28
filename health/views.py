from django import views
from django.shortcuts import redirect, render
from django.views import generic

from health.forms import AppointmentForm


def home(request):
    return render(request, "home.html", {})


class HomeView(generic.TemplateView):
    template_name = "home.html"


def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AppointmentForm()

    return render(
        request,
        "home.html",
        {
            "form": form,
            "title": "Make an Appointment with DentaCare",
            "heading": "Make an Appointment",
        },
    )


def contact(request):
    return render(request, "contact.html", {})
