from django.urls import path, include
from .views import messageList, userList, MessageViewSet, UserViewSet
from rest_framework import routers
from django.urls import re_path
router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/messages/<sender>/<receiver>', messageList, name='messages'),
    path('api/users/<int:pk>', userList, name='user'),
    path('api/users/', userList, name='users'),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
]