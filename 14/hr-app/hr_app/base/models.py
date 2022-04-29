from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lastName

    class Meta:
        ordering = ['approved']