from django.db import models
from django.contrib.auth.models import User
from neighborhoods.models import Neighborhood


class Business(models.Model):
    name = models.CharField(max_length=55, unique=True)
    user = models.ForeignKey(
        User, related_name='owner', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(
        Neighborhood, related_name='hood', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    established = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_business(cls, id):
        business = cls.objects.get(id=id)
        return business

    def create_business(self):
        self.save()
        return self

    @classmethod
    def delete_business(cls, id):
        business = cls.objects.get(id=id).delete()
        return business

    @classmethod
    def update_business(cls, obj):
        business = cls.get_business(obj.id)
        business.name = obj.name
        business.neighborhood = obj.neighborhood
        business.email = obj.email
        business.save()
        return business


def __str__(self):
    return self.name
