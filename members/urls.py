from django.urls import path
from .views import UserRegisterView, UserEditView, Password_ChangeView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit_settings/', UserEditView.as_view(), name = 'edit_settings'),
    path('password/', Password_ChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),
]