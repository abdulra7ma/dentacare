from typing import Any
from django import views
from django.shortcuts import redirect, render
from django.views import generic

from health.forms import AppointmentForm, ContactMessagePageForm
from health.models import Appointment, Blog, Doctor
from django.views.generic.edit import CreateView


class HomeView(generic.TemplateView):
    template_name = "home.html"


class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactMessagePageForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BlogView(generic.ListView):
    template_name = "blog.html"
    queryset = Blog.objects.all()
    context_object_name = "blogs"


class BlogDetailView(generic.DetailView):
    template_name = "blog_detail.html"
    model = Blog
    context_object_name = "blog"


class AboutView(generic.TemplateView):
    template_name = "about.html"


class ServicesView(generic.TemplateView):
    template_name = "services.html"


class DoctorsView(generic.ListView):
    template_name = "doctors.html"
    queryset = Doctor.objects.all()
    context_object_name = "doctors"


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "home.html"
    success_url = "/" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Make an Appointment with DentaCare Experience"
        context["heading"] = "Make an Appointment"
        return context

    def get_initial(self) -> dict[str, Any]:
        return super().get_initial()
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)


def contact(request):
    return render(request, "contact.html", {})
