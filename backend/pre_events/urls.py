from django.urls import path
from django.conf.urls import url, include

from .views import *

urlpatterns = [
	path('consult_events/', consult_events, name='consult_events'),
	path('proponent_events/', proponent_events, name='proponent_events'),
	path('admin_events/', admin_events, name='admin_events'),
	path('delete_event/<int:id>', delete_event, name='delete_event'),
	path('event_details/<int:id>', event_details, name='event_details'),
	path('event_logistics_form/<int:id>', event_logistics_form, name='event_logistics_form'),
	path('view_event_logistic/<int:id>', view_event_logistic, name='view_event_logistic'),
	path('delete_event_logistic/<int:id>', delete_event_logistic, name='delete_event_logistic'),
	path('attrib_equipment/<int:id>', attrib_equipment, name='attrib_equipment'),
	path('attrib_service/<int:id>', attrib_service, name='attrib_service'),
	path('attrib_location/<int:id>', attrib_location, name='attrib_location'),
	path('event_logistic_list/<int:id>', event_logistic_list, name='event_logistic_list'),
	path('change_logistic_equipment/<int:id>', change_logistic_equipment, name='change_logistic_equipment'),
	path('change_logistic_location/<int:id>', change_logistic_location, name='change_logistic_location'),
	path('change_logistic_service/<int:id>', change_logistic_service, name='change_logistic_service'),
	path('create_event/', create_event, name='create_event'),
	path('delete_service/<int:id>/<int:num>', delete_service, name='delete_service'),
	path('delete_equipment/<int:id>/<int:num>', delete_equipment, name='delete_equipment'),
	path('delete_location/<int:id>/<int:num>', delete_location, name='delete_location'),
	path('validate_equipment/<int:id>', validate_equipment, name='validate_equipment'),
	path('validate_service/<int:id>', validate_service, name='validate_service'),
	path('validate_location/<int:id>', validate_location, name='validate_location'),
	path('invalidate_equipment/<int:id>', invalidate_equipment, name='invalidate_equipment'),
	path('invalidate_service/<int:id>', invalidate_service, name='invalidate_service'),
	path('invalidate_location/<int:id>', invalidate_location, name='invalidate_location'),
	path('delete_attrib_location/<int:id>', delete_attrib_location, name='delete_attrib_location'),
	path('delete_attrib_equipment/<int:id>', delete_attrib_equipment, name='delete_attrib_equipment'),
	path('delete_attrib_service/<int:id>', delete_attrib_service, name='delete_attrib_service'),
	path('validate_logistics/<int:id>', validate_logistics, name="validate_logistics"),
	path('end_events/<int:id>', end_event, name="end_event")
]
