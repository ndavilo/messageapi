from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import PasswordInput



class SignUpForm(UserCreationForm):
	email 		=	forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

	class Meta:
		model 	=	User
		fields 	=	('username', 'email', 'password1', 'password2')


	def __init__ (self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditSettingsForm(UserChangeForm):
	email 		=	forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password 	=	forms.CharField(required=False, max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Click on Change password bellow'}))



	class Meta:
		model 	=	User
		fields 	=	('email',)

class PasswordChangingForm(PasswordChangeForm):
	old_password 		=	forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
	new_password1		=	forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'})) 
	new_password2		=	forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

	class Meta:
		model 	=	User
		fields 	=	('old_password', 'new_password1', 'new_password2')