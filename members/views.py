from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditSettingsForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class UserRegisterView(generic.CreateView):
	form_class 		=	SignUpForm
	template_name 	= 	'registration/register.html' 
	success_url		=	reverse_lazy('login')

class UserEditView(generic.UpdateView):
	form_class 		=	EditSettingsForm
	template_name 	= 	'registration/edit_settings.html'
	success_url		=	reverse_lazy('group')

	def get_object(self):
		return self.request.user

class Password_ChangeView(PasswordChangeView):
	
	form_class		=	PasswordChangingForm #PasswordChangeForm
	success_url		=	reverse_lazy('password_success')

def password_success(request):
	return render(request, 'registration/password_success.html', {})