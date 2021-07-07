from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.urls import reverse
from django.contrib import messages
from django.db import connection
from django.conf import settings
from django.contrib.auth.models import Group

from users.forms import SignupForm, GeneralUserForm, ParticipantForm, AdministratorForm,ProponentForm 
from resources.models import Generaluser

# Create your views here.

def dashboard(request):
	return render(request, "users/dashboard.html")

def register(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if(form.is_valid()):
			user = form.save()
			gabinete = form.cleaned_data['gabinete']
			login(request, user)
			user_ptr = get_user_model().objects.get(id=request.user.id)
			data = { 
				'user_ptr': user_ptr,
				'contact': form.cleaned_data['contact']
			}
			general_user_form = GeneralUserForm(data)
			general_user_form.save()

			general_user = Generaluser.objects.get(user_ptr_id=request.user.id)

			fields = form.cleaned_data['user_field']

			for field in fields:
				group = Group.objects.get(id=field)
				group_data = { "user": user_ptr, "group": group}
				# auth_user_group_form = AuthUserGroupsForm(group_data)
				# auth_user_group_form.save()
				group.user_set.add(user)
				if group.name == 'participant':
					data_participant = { "generaluser_ptr":general_user }
					participant_form = ParticipantForm(data_participant)
					if(participant_form.is_valid()):
						participant_form.save()
				elif group.name == 'proponent':
					data_proponent = { "generaluser_ptr":general_user }
					proponent_form = ProponentForm(data_proponent)
					if(proponent_form.is_valid()):
						proponent_form.save()
				else:
					data_administrator = { "generaluser_ptr":general_user, "gabinete": gabinete }
					administrator_form = AdministratorForm(data_administrator)
					if(administrator_form.is_valid()):
						administrator_form.save()
				
			return redirect('dashboard')
		else:
			messages.error(request, form.errors.as_ul)
			print(form.errors)
			print(form.non_field_errors)
	else:
		form = SignupForm()
	
	return render(request, 'registration/register.html', {'form': form})