import profile
from django.contrib.auth.models import User
from neighborhoods.models import Neighborhood
from businesses.models import Business
from rest_framework import serializers
from posts.models import Post, Comment
from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UpateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', ]


class NeighborhoodSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='neighbors-detail')
    admin = serializers.StringRelatedField()

    class Meta:
        model = Neighborhood
        fields = [
            'url',
            'name',
            'location',
            'occupants',
            'admin',
            'id'
        ]


class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='businesses-detail')
    user = serializers.StringRelatedField()
    neighborhood = serializers.StringRelatedField()

    class Meta:
        model = Business
        fields = [
            'name',
            'user',
            'email',
            'neighborhood',
            'id',
            'url',
            'established'
        ]


class CommentSerialzer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='comments-detail')
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), required=False)
    likes = UserSerializer(many=True, required=False)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'post',
            'comment',
            'id',
            'likes',
            'user',
            'posted_at',
            'url',
        ]

    def get_user(self, obj):
        profile = Profile.objects.get(id=obj.user.id)
        user = {
            "id": obj.user.id,
            "username": obj.user.username,
            'email': obj.user.email,
            "image": f"{profile.image.url}"
        }
        return user


class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='posts-detail')
    user = serializers.SerializerMethodField()
    comments = CommentSerialzer(many=True, required=False)
    likes = UserSerializer(many=True, required=False)
    neighborhood = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = [
            'post',
            'comments',
            'neighborhood',
            'user',
            'likes',
            'id',
            'url',
            'image',
            'posted_at'
        ]

    def get_user(self, obj):
        profile = Profile.objects.get(id=obj.user.id)
        user = {
            "id": obj.user.id,
            "username": obj.user.username,
            'email': obj.user.email,
            "image": f"{profile.image.url}"
        }
        return user


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UpateUserSerializer(required=False)
    posts = PostSerializer(many=True, read_only=True)
    neighborhood = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = [
            # 'url',
            'id',
            'user',
            'bio',
            'posts',
            'neighborhood',
            'image',
        ]

    def get_neighborhood(self, obj):
        return obj.neighborhood.id

