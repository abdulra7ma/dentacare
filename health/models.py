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
