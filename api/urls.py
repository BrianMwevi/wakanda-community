from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import BusinessViewset, CommentViewset, NeighborhoodViewset, PostViewset, UserCreate, ProfileViewset, LoginAPI, UpdateUser

from django.urls import path

from knox import views as knox_views

router = DefaultRouter()
router.register('neighborhoods', NeighborhoodViewset, basename='neighbors')
router.register('businesses', BusinessViewset, basename='businesses')
router.register('posts', PostViewset, basename='posts')
router.register('comments', CommentViewset, basename='comments')

urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path('profile/', ProfileViewset.as_view(), name='profile'),
    path('profile/<int:id>/', ProfileViewset.as_view(), name='profile_update'),

    path('profile/user/<int:id>/', UpdateUser.as_view(), name='user_update'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]

urlpatterns += router.urls
