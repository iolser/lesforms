from django.urls import path
from django.conf.urls import url, include
from events.views import *

urlpatterns = [
	path("registrations/", registrations, name='registrations'),
	path('cancel_registration/<int:id>', cancel_registration, name='cancel_registration'),
]
