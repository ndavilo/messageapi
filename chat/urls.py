from django.urls import path, include
from .views import group, RoomView, checkview, SendGroupMessage, AddAllowedUserView, UserViewSet, MessageViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'message', MessageViewSet)

urlpatterns = [
    path('home/', group, name='group'),
    path('<str:room>/<int:pk>/', RoomView.as_view(), name='room'),
    path('checkview', checkview, name='checkview'),
    path('<str:room>/<int:pk>/send', SendGroupMessage.as_view(), name='send'),
    path('<str:room>/<int:pk>/addusers', AddAllowedUserView.as_view(), name='addusers'),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
]