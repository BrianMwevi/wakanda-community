from django.db import models
from django.contrib.auth.models import User
from neighborhoods.models import Neighborhood


class Post(models.Model):
    user = models.ForeignKey(
        User, related_name='author', on_delete=models.CASCADE)
    post = models.TextField()
    comments = models.ManyToManyField(
        'Comment', related_name='comments', blank=True)
    likes = models.ManyToManyField(
        User, related_name='post_likes', blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    likes = models.ManyToManyField(
        User, blank=True, related_name='comment_likes')
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
