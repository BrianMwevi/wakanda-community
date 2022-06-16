from django.db import models
from django.contrib.auth.models import User


class Neighborhood(models.Model):
    name = models.CharField(max_length=55)
    location = models.CharField(max_length=55, blank=False, null=False)
    occupants = models.IntegerField(default=1, blank=True, null=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return self.location