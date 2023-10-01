from django.urls import path
from . import views

urlpatterns = [
    path("", views.appointment, name="home"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("blog/", views.BlogView.as_view(), name="blog"),
    path(
        "blog/<int:blog_id>/", views.BlogDetailView.as_view(), name="blog_detail"
    ),
    path("about/", views.AboutView.as_view(), name="about"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("doctors/", views.DoctorsView.as_view(), name="doctors"),
]
