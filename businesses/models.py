from django.db import models
from django.contrib.auth.models import User
from neighborhoods.models import Neighborhood


class Business(models.Model):
    name = models.CharField(max_length=55, unique=True,
                            blank=False, null=False)
    user = models.ForeignKey(
        User, related_name='owner', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(
        Neighborhood, related_name='hood', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    established = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.name
