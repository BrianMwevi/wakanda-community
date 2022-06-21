from ast import Is
import email
import profile
from urllib import request
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions, status
from django.contrib.auth    .models import User

from neighborhoods.models import Neighborhood
from posts.models import Post, Comment
from businesses.models import Business
from accounts.models import Profile

from .serializers import BusinessSerializer, CommentSerialzer, NeighborhoodSerializer, PostSerializer, UserSerializer, ProfileSerializer, UpateUserSerializer

from django.contrib.auth import login

from knox.views import LoginView as KnoxLoginView


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'
    serializer_class = UpateUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(username=self.request.user.username)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class ProfileViewset(generics.RetrieveUpdateDestroyAPIView):
    # class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "id"
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=request.user.id)
        data = ProfileSerializer(profile, context={
                                 'request': request}).data
        return Response(data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        neighborhood = self.request.data.get('neighborhood', None)
        if neighborhood:
            neighborhood = Neighborhood.objects.get(
                id=self.request.data['neighborhood'])
            serializer.save(neighborhood=neighborhood, user=self.request.user)
        else:
            serializer.save(user=self.request.user)


class NeighborhoodViewset(viewsets.ModelViewSet):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        neighborhood = serializer.save(admin=self.request.user)
        neighborhood.occupants.add(request.user)
        profile.neighborhood = neighborhood
        profile.save()


class BusinessViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def perform_create(self, serializer):
        neighborhood = Neighborhood.objects.get(
            id=self.request.data['neighborhood'])
        serializer.save(user=self.request.user, neighborhood=neighborhood)


class PostViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        neighborhood = self.request.user.profile.neighborhood
        posts = Post.objects.filter(neighborhood=neighborhood)
        return posts

    def perform_create(self, serializer):
        neighborhood = Neighborhood.objects.get(
            id=self.request.data['neighborhood'])
        post = serializer.save(user=self.request.user,
                               neighborhood=neighborhood)
        self.request.user.profile.posts.add(post)


class CommentViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = CommentSerialzer

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.request.data['post'])
        comment = serializer.save(user=self.request.user, post=post)
        post.comments.add(comment)
