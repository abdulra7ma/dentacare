from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

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
            ("Teeth Whiteing", "teeth_whiteing"),
            ("Teeth Cleaning", "teeth_cleaning"),
            ("Quality Brackets", "quality_brackets"),
            ("Modern Anesthetic", "modern_anesthetic"),
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
