from django import views
from django.shortcuts import redirect, render
from django.views import generic

from health.forms import AppointmentForm
from health.models import Doctor


class HomeView(generic.TemplateView):
    template_name = "home.html"


class ContactView(generic.TemplateView):
    template_name = "contact.html"


class BlogView(generic.TemplateView):
    template_name = "blog.html"
    

class BlogDetailView(generic.TemplateView):
    template_name = "blog_detail.html"


class AboutView(generic.TemplateView):
    template_name = "about.html"


class ServicesView(generic.TemplateView):
    template_name = "services.html"
    
    
class DoctorsView(generic.ListView):
    template_name = "doctors.html"
    queryset = Doctor.objects.all()
    context_object_name = "doctors"
    
    
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
