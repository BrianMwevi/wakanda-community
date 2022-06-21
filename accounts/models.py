from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from neighborhoods.models import Neighborhood
from posts.models import Post
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True)
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(
        upload_to='images/', default="images/avatar_wqbvxp.svg")

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username
