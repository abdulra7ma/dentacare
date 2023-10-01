from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(
        max_length=100,
        choices=[
            ("dentist", "Dentist"),
            ("doctor", "Doctor"),
            ("nurse", "Nurse"),
            ("therapist", "Therapist"),
            ("system_analyst", "System Analyst"),
        ],
    )
    description = models.TextField()
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    google_plus = models.URLField(blank=True, null=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="images/", blank=True, null=True
    )

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    department = models.CharField(
        max_length=100,
        choices=[
            ("teeth_whiteing", "Teeth Whiteing"),
            ("teeth_cleaning", "Teeth Cleaning"),
            ("quality_brackets", "Quality Brackets"),
            ("modern_anesthetic", "Modern Anesthetic"),
        ],
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        """
        Returns a string representation of the object's name.

        :return: The name of the object as a string.
        """
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        """
        Returns a string representation of the object's title.

        :return: The title of the object as a string.
        """
        return self.title