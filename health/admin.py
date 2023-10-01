from django.contrib import admin
from .models import Doctor, Appointment, Blog, Category, ContactMessage


admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(ContactMessage)