from django import forms
from .models import Appointment, ContactMessage


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["department"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "appointment_name",
                "placeholder": "Name",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "appointment_email",
                "placeholder": "Email",
            }
        )
        self.fields["date"].widget.attrs.update(
            {"class": "form-control appointment_date", "placeholder": "Date"}
        )
        self.fields["time"].widget.attrs.update(
            {"class": "form-control appointment_time", "placeholder": "Time"}
        )
        self.fields["phone"].widget.attrs.update(
            {"class": "form-control", "id": "phone", "placeholder": "Phone"}
        )


class ContactMessagePageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "appointment_name",
                "placeholder": "Name",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "appointment_email",
                "placeholder": "Email",
            }
        )
        self.fields["subject"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "subject",
                "placeholder": "Subject",
            }
        )
        self.fields["message"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "message",
                "placeholder": "Message",
                "rows": "7",
                "cols": "30",
            }
        )