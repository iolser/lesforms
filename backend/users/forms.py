from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.validators import RegexValidator

from resources.models import Generaluser, Participant, Administrator, Proponent
groups = Group.objects.all()

signup_dict = {}

for group in groups:
	key = str(group.pk)
	value = str(group.name)
	signup_dict[key] = value

signup_choices = [(k, v) for k, v in signup_dict.items()]

class SignupForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required.')

	#	Regex magic for the contact field
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	contact = forms.CharField(validators=[phone_regex], max_length=20, required=False)
	gabinete = forms.CharField(max_length=255, required=False, help_text='Optional.')

	user_field = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=signup_choices, label="Tipo de utilizador")

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'contact', 'gabinete', 'password1', 'password2', 'user_field')

class GeneralUserForm(forms.ModelForm):
	class Meta:
		model = Generaluser
		fields = {'user_ptr', 'contact'}

# class AuthUserGroupsForm(forms.ModelForm):
# 	class Meta:
# 		model = AuthUserGroups
# 		fields = {'user', 'group'}



class ParticipantForm(forms.ModelForm):
	class Meta:
		model = Participant
		fields = {'generaluser_ptr'}

class AdministratorForm(forms.ModelForm):
	class Meta:
		model = Administrator
		fields = {'generaluser_ptr', 'gabinete'}

class ProponentForm(forms.ModelForm):
	class Meta:
		model = Proponent
		fields = {'generaluser_ptr'}