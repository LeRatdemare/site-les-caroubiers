from django.db import models

# Create your models here.
class Family(models.Model):

    name = models.CharField(max_length=50)
    has_child_in_college = models.BooleanField(default=False)
    has_child_in_school = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
