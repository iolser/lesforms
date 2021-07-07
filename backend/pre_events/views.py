from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, QueryDict
from django.core import serializers
from notificacoes.views import *
from resources.models import *
from pre_events.forms import *
from forms.models import FormAnswer

# import json, datetime

# Create your views here.

def consult_events(request):
	if not Participant.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	events = Event.objects.all()
	registered = FormAnswer.objects.filter(
		answerer=request.user.id
	)
	return render(request, 'consult_events.html', {'events' : events, 'registered' : [r.event for r in registered]})

def proponent_events(request):
	if not Proponent.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	events = Event.objects.filter(organizer=request.user.id)
	return render(request, 'proponent_events.html', {'events': events})

def admin_events(request):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	events = Event.objects.all()
	return render(request, 'admin_events.html', {'events': events})

def create_event(request):
	if not Proponent.objects.filter(generaluser_ptr=request.user.id).exists() and not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	if request.method == 'POST':
		form = EventForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, "Evento criado com sucesso!")
			return redirect("consult_events")
		else:
			messages.error(request, "Formulário inválido")
	else:
		form = EventForm()

	return render(request, 'create_event.html', {"form": form})

def delete_event(request, id):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	event = Event.objects.filter(id=id)
	event.delete()
	messages.success(request, 'Evento eliminado com sucesso!')
	return redirect('consult_events')

def event_details(request, id):
	event = Event.objects.get(id=id)
	form = event.eventtype.formproposalid
	answers = FormAnswer.objects.filter(event=event)
	answers_proposal = []
	for a in answers:
		if a.form.type.id == 2:
			answers_proposal.append(a)
	return render(request, 'event_details.html', {'event' : event, "form": form, "proposal":  answers_proposal[0] if len(answers_proposal) > 0 else None})

def event_logistics_form(request, id):
	if not Event.objects.filter(id=id, organizer__generaluser_ptr__user_ptr=request.user).exists() and not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect("/")
	event = Event.objects.get(id=id)

	if(request.method == 'POST'):
		services_formset = RequestServicesFormset(request.POST, prefix='services')
		equips_formset = RequestEquipmentFormset(request.POST, prefix='equips')
		locations_formset = RequestLocationFormset(request.POST, prefix='locations')

		for form in services_formset:
			form.instance.event = event

		for form in equips_formset:
			form.instance.event = event

		for form in locations_formset:
			form.instance.event = event

		if(services_formset.is_valid() and equips_formset.is_valid() and locations_formset.is_valid()):
			for form in services_formset.forms:
				if form.cleaned_data["servicestype"] is None:
					messages.error(request, "Por favor selecione o tipo de serviço.")
					return redirect("event_logistics_form", event.id)

			for form in services_formset.forms:
				if form.cleaned_data["servicestype"] is None:
					messages.error(request, "Por favor selecione o tipo de equipamento.")
					return redirect("event_logistics_form", event.id)

			for form in services_formset.forms:
				if form.cleaned_data["servicestype"] is None:
					messages.error(request, "Por favor selecione o tipo de localização.")	
					return redirect("event_logistics_form", event.id)

			services_formset.save()
			equips_formset.save()
			locations_formset.save()

			event.state = 3
			event.save()
			messages.success(request, "Logística submetida com sucesso!")
			return redirect("event_details", id=id)
	else:
		services_formset = RequestServicesFormset(queryset=Requestservices.objects.none(), prefix='services')
		equips_formset = RequestEquipmentFormset(queryset=Requestequipment.objects.none(), prefix='equips')
		locations_formset = RequestLocationFormset(queryset=Requestlocation.objects.none(), prefix='locations')
	
	return render(request, 'logistics_form.html', {'equipsformset' : equips_formset, 'servicesformset':services_formset, 'locationsformset':locations_formset})


def view_event_logistic(request, id):
	if not Event.objects.filter(id=id, organizer__generaluser_ptr__user_ptr=request.user).exists() and not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	event = Event.objects.get(id=id)
	services = Requestservices.objects.filter(event=id)
	equipments = Requestequipment.objects.filter(event=id)
	locations = Requestlocation.objects.filter(event=id)
	
	return render(request, 'view_event_logistic.html', {"services": services, "equipments": equipments, "locations": locations, "event": event})

def event_logistic_list(request, id):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	event = Event.objects.get(id=id)
	services = Serviceuse.objects.filter(event=id)
	equipments = Itemuse.objects.filter(event=id)
	locations = Locationuse.objects.filter(event=id)
	
	return render(request, 'event_logistic_list.html', {"services": services, "equipments": equipments, "locations": locations, "event": event})

def delete_event_logistic(request, id):
	if not Event.objects.filter(id=id, organizer__generaluser_ptr__user_ptr=request.user).exists() and not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	event = Event.objects.get(id=id)
	services = Requestservices.objects.filter(event=id)
	equipments = Requestequipment.objects.filter(event=id)
	locations = Requestlocation.objects.filter(event=id)

	services.delete()
	equipments.delete()
	locations.delete()

	event.state = 1
	event.save()

	messages.success(request, "Logística eliminada com sucesso!")
	return redirect("event_details", id=id)

def change_logistic_service(request, id):
	if not Event.objects.filter(id=id, organizer__generaluser_ptr__user_ptr=request.user).exists() and not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	service_request = Requestservices.objects.get(id=id)

	form = RequestServicesForm({
		'start' : service_request.start.strftime('%Y-%m-%dT%H:%M'),
		'end' : service_request.end.strftime('%Y-%m-%dT%H:%M'),
		'quantity' : service_request.quantity
	})

	if(request.method == 'POST'):
		form = RequestServicesForm(request.POST)

		if(form.is_valid()):
			service_request.start = form.instance.start
			service_request.end = form.instance.end
			service_request.quantity = form.instance.quantity

			service_request.save()
			return redirect('view_event_logistic', service_request.event.id)
	
	return render(request, 'change_event_logistic.html', { "form" : form, "name" : "serviço",  "id_name" : "id_servicestype", "selected_id" : service_request.servicestype.id })

def change_logistic_equipment(request, id):
	if not Event.objects.filter(id=id, organizer__generaluser_ptr__user_ptr=request.user).exists() and not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	equipment_request = Requestequipment.objects.get(id=id)

	form = RequestEquipmentForm({
		'start' : equipment_request.start.strftime('%Y-%m-%dT%H:%M'),
		'end' : equipment_request.end.strftime('%Y-%m-%dT%H:%M'),
		'quantity' : equipment_request.quantity
	})

	if(request.method == 'POST'):
		form = RequestEquipmentForm(request.POST)
		
		if(form.is_valid()):
			equipment_request.start = form.instance.start
			equipment_request.end = form.instance.end
			equipment_request.quantity = form.instance.quantity

			equipment_request.save()
			return redirect('view_event_logistic', equipment_request.event.id)
	
	return render(request, 'change_event_logistic.html', { "form" : form, "name" : "equipamento",  "id_name" : "id_typeequipment", "selected_id" : equipment_request.typeequipment.id })

def change_logistic_location(request, id):
	if not Event.objects.filter(id=id, organizer__generaluser_ptr__user_ptr=request.user).exists() and not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	location_request = Requestlocation.objects.get(id=id)

	form = RequestLocationForm({
		'start' : location_request.start.strftime('%Y-%m-%dT%H:%M'),
		'end' : location_request.end.strftime('%Y-%m-%dT%H:%M'),
		'quantity' : location_request.quantity
	})

	if(request.method == 'POST'):
		form = RequestLocationForm(request.POST)

		if(form.is_valid()):
			location_request.start = form.instance.start
			location_request.end = form.instance.end
			location_request.quantity = form.instance.quantity

			location_request.save()
			return redirect('view_event_logistic', location_request.event.id)
	
	return render(request, 'change_event_logistic.html', { "form" : form, "name" : "espaço",  "id_name" : "id_locationtype", "selected_id" : location_request.locationtype.id})



def delete_attrib_equipment(request, id):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	obj = Itemuse.objects.get(id=id)
	enviar_notificacao_automatica(request, NotificationAddr.RECUSAR_LOGISTICA_EQUIP, obj.id)
	obj.delete()
	messages.success(request, "Equipamento atribuído eliminado com sucesso!")
	return redirect('event_logistic_list', obj.event.id)


def delete_attrib_service(request, id):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	obj = Serviceuse.objects.get(id=id)
	enviar_notificacao_automatica(request, NotificationAddr.RECUSAR_LOGISTICA_SERVICE, obj.id)
	obj.delete()
	messages.success(request, "Serviço atribuído eliminado com sucesso!")
	return redirect('event_logistic_list', obj.event.id)


def delete_attrib_location(request, id):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	obj = Locationuse.objects.get(id=id)
	enviar_notificacao_automatica(request, NotificationAddr.RECUSAR_LOGISTICA_LOCATION, obj.id)
	obj.delete()
	messages.success(request, "Espaço atribuído eliminado com sucesso!")
	return redirect('event_logistic_list', obj.event.id)

def attrib_equipment(request, id):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	requestequip = Requestequipment.objects.get(id=id)

	event = Event.objects.get(id=requestequip.event.id)

	items = Item.objects.filter(typeequipment=requestequip.typeequipment)

	allequipmentuses = Itemuse.objects
	
	allequipments = allequipmentuses.filter(start__lte=requestequip.start, end__gte=requestequip.start) | allequipmentuses.filter(start__gte=requestequip.start, end__gte=requestequip.end) | allequipmentuses.filter(start__gte=requestequip.start, end__lte=requestequip.end) | allequipmentuses.filter(start__lte=requestequip.start, end__gte=requestequip.end) 
	
	for equipmentuse in allequipments:
		if items.filter(id=equipmentuse.item.id).exists() :
			items = items.exclude(id=equipmentuse.item.id)

	if request.method == 'POST':
		form = ItemuseForm(request.POST)
		item = request.POST['item']
		

		form.instance.item = Item.objects.get(id=item)
		form.instance.event = event

		if form.is_valid():
			obj = form.save()

			requestequip.quantity = requestequip.quantity-1

			if requestequip.quantity == 0:
				requestequip.delete()
			else:
				requestequip.save()

			enviar_notificacao_automatica(request, NotificationAddr.ATRIBUIR_LOGISTICA_EQUIP, obj.id)
			messages.success(request, 'Equipamento atribuido com sucesso!')  
			return redirect('view_event_logistic', id=event.id)
		else:
			messages.error(request, 'Formulario inválido!')
	else:
		form = ItemuseForm({
			'start' : requestequip.start.strftime('%Y-%m-%dT%H:%M'),
			'end' : requestequip.end.strftime('%Y-%m-%dT%H:%M')
		})
	
	return render(request, 'logistic_validate_equipment.html', {'form' : form, 'requestequip': requestequip, 'items' : items, 'event' : event})

def attrib_service(request, id):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	requestserv = Requestservices.objects.get(id=id)

	event = Event.objects.get(id=requestserv.event.id)

	services = Service.objects.filter(servicestype=requestserv.servicestype)

	allservicesuses = Serviceuse.objects
	
	allservices = allservicesuses.filter(start__lte=requestserv.start, end__gte=requestserv.start) | allservicesuses.filter(start__gte=requestserv.start, end__gte=requestserv.end) | allservicesuses.filter(start__gte=requestserv.start, end__lte=requestserv.end) | allservicesuses.filter(start__lte=requestserv.start, end__gte=requestserv.end) 
	

	print(allservices)

	for serviceuse in allservices:
		if services.filter(id=serviceuse.service.id).exists() :
			services = services.exclude(id=serviceuse.service.id)

	if request.method == 'POST':
		form = ServiceuseForm(request.POST)
		service = request.POST['service']
		

		form.instance.service = Service.objects.get(id=service)
		form.instance.event = event

	

		if form.is_valid():
			obj = form.save()


			requestserv.quantity = requestserv.quantity-1

			if requestserv.quantity == 0:
				requestserv.delete()
			else:
				requestserv.save()

			enviar_notificacao_automatica(request, NotificationAddr.ATRIBUIR_LOGISTICA_SERVICE, obj.id)
			messages.success(request, 'Serviço atribuido com sucesso!')  
			return redirect('view_event_logistic', id=event.id)
		else:
			messages.error(request, 'Formulario inválido!')
	else:
		form = ServiceuseForm({
			'start' : requestserv.start.strftime('%Y-%m-%dT%H:%M'),
			'end' : requestserv.end.strftime('%Y-%m-%dT%H:%M')
		})
	
	return render(request, 'logistic_validate_service.html', {'form' : form, 'requestserv': requestserv, 'services' : services,'event' : event})


def attrib_location(request, id):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	requestlocation = Requestlocation.objects.get(id=id)

	event = Event.objects.get(id=requestlocation.event.id)

	locations = Location.objects.filter(locationtype=requestlocation.locationtype)

	alllocationuses = Locationuse.objects
	
	alllocations = alllocationuses.filter(start__lte=requestlocation.start, end__gte=requestlocation.start) | alllocationuses.filter(start__gte=requestlocation.start, end__gte=requestlocation.end) | alllocationuses.filter(start__gte=requestlocation.start, end__lte=requestlocation.end) | alllocationuses.filter(start__lte=requestlocation.start, end__gte=requestlocation.end) 
	
	for locationuse in alllocations:
		if locations.filter(id=locationuse.location.id).exists() :
			locations = locations.exclude(id=locationuse.location.id)

	if request.method == 'POST':
		form = LocationuseForm(request.POST)
		location = request.POST['location']
		

		form.instance.location = Location.objects.get(id=location)
		form.instance.event = event

		if form.is_valid():
			obj = form.save()

			requestlocation.quantity = requestlocation.quantity-1
			
			if requestlocation.quantity == 0:
				requestlocation.delete()
			else:
				requestlocation.save()
			
			print(obj.id)
			enviar_notificacao_automatica(request, NotificationAddr.ATRIBUIR_LOGISTICA_LOCATION, obj.id)
			messages.success(request, 'Espaço atribuido com sucesso!')  
			return redirect('view_event_logistic', id=event.id)
		else:
			messages.error(request, 'Formulario inválido!')
	else:
		form = LocationuseForm({
			'start' : requestlocation.start.strftime('%Y-%m-%dT%H:%M'),
			'end' : requestlocation.end.strftime('%Y-%m-%dT%H:%M')
		})
	
	return render(request, 'logistic_validate_location.html', {'form' : form, 'requestlocation': requestlocation, 'locations' : locations, 'event' : event})

def validate_logistics(request, id):
	if not Administrator.objects.filter(generaluser_ptr=request.user.id).exists():
		return redirect('/')
	event = Event.objects.get(id=id)
	event.state = 4
	event.save()
	return redirect("event_details", id)

def end_event(request, id):
	event = Event.objects.get(id=id)
	event.state = 5
	event.save()
	return redirect("event_details", id)

# Views para apagar pedidos de logistica

def delete_service(request, id, num):
	service = Requestservices.objects.filter(id=id)
	service.delete()
	return redirect("view_event_logistic", id=num)

def delete_equipment(request, id, num):
	equipment = Requestequipment.objects.filter(id=id)
	equipment.delete()
	return redirect("view_event_logistic", id=num)

def delete_location(request, id, num):
	location = Requestlocation.objects.filter(id=id)
	location.delete()
	return redirect("view_event_logistic", id=num)

def validate_service(request, id):
	service = Requestservices.objects.get(id=id)
	service.valid = True
	service.save()
	return redirect("view_event_logistic", id=service.event.id)

def invalidate_service(request, id):
	service = Requestservices.objects.get(id=id)
	service.valid = False
	service.save()
	return redirect("view_event_logistic", id=service.event.id)

def validate_equipment(request, id):
	equipment = Requestequipment.objects.get(id=id)
	equipment.valid = True
	equipment.save()
	return redirect("view_event_logistic", id=equipment.event.id)

def invalidate_equipment(request, id):
	equipment = Requestequipment.objects.get(id=id)
	equipment.valid = False
	equipment.save()
	return redirect("view_event_logistic", id=equipment.event.id)

def validate_location(request, id):
	location = Requestlocation.objects.get(id=id)
	location.valid = True
	location.save()
	return redirect("view_event_logistic", id=location.event.id)

def invalidate_location(request, id):
	location = Requestlocation.objects.get(id=id)
	location.valid = False
	location.save()
	return redirect("view_event_logistic", id=location.event.id)