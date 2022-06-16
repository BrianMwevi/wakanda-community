from django.db import models
from django.contrib.auth.models import User


class Neighborhood(models.Model):
    name = models.CharField(max_length=55)
    location = models.CharField(max_length=55)
    occupants = models.IntegerField(default=1, blank=True, null=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_neighborhood(cls, id):
        neighborhood = cls.objects.get(id=id)
        return neighborhood

    def create_neighborhood(self):
        self.save()
        return self

    @classmethod
    def delete_neighborhood(cls, id):
        neighborhood = cls.objects.get(id=id).delete()
        return neighborhood

    @classmethod
    def update_neighborhood(cls, obj):
        neighborhood = cls.get_neighborhood(obj.id)
        neighborhood.name = obj.name
        neighborhood.location = obj.location
        neighborhood.save()
        return neighborhood

    def update_occupants(self, occupants):
        self.occupants += occupants
        self.save()
        return self

    def __str__(self):
        return self.location
