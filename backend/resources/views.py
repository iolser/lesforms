from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
import json
from django.http import JsonResponse



# Create your views here.

from .forms import *
from .models import *

def equipment(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = equipmentForm(request.POST)
		# print(str(form.data['imageURL']) + '\n')
		# print()
		# check whether it's valid:

		if(Typeequipment.objects.filter(name = form.data["name"])):
			messages.error(request, 'Equipamento já existe!')
		else:
			if form.is_valid():
				print("is")
				# wtv = Typeequipment(name=form.data['equipmentName'], image= form.data['imageURL'])
				# wtv.save()
				image = request.POST.get("imageURL")
				if(image is not None):
					equip = Typeequipment(name = form.instance.name, image=image)
					equip.save()
				else:
					form.save()
				
				messages.success(request, 'Equipamento adicionado com sucesso!')
				return redirect('equipmentList')
			else:
				if form.errors.as_data().__contains__('name'):
					messages.error(request, 'O nome que tentou inserir já existe.')
				else:
					messages.error(request, 'Formulario inválido!')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = equipmentForm()
	return render(request, 'equipment.html', {'form': form})

def equipmentList(request):
	
	query = Typeequipment.objects.all()


	print(query)
	
	return render(request, 'equipmentList.html', {'query': query})

def equipmentDelete(request, id):
	query = Typeequipment.objects.get(id=id)
	query.delete()
	messages.success(request, 'Equipamento eliminado com sucesso!')
	return redirect('equipmentList')


def equipmentEdit(request, id):
	obj = Typeequipment.objects.get(id=id)
	if request.method == 'POST':
		form = equipmentForm(request.POST, instance=obj)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			messages.success(request, 'Equipamento editado com sucesso!')
			return redirect('equipmentList')
		else:
			if form.errors.as_data().__contains__('name'):
				messages.error(request, 'O nome que tentou inserir já existe.')
			else:
				messages.error(request, 'Formulario inválido!')
	else:
		form = equipmentForm(
		{
			'name' : str(obj.name),
			'image' : str(obj.image),		
		}
		)
	
	return render(request, 'equipmentEdit.html', {'obj' : obj, 'form' : form})

# def locationType(request):
#     if request.method == 'POST':
#         form = locationTypeForm(request.POST)
#         if form.is_valid():
		
#             messages.success(request, 'Campus inserido!')
#             return render(request, 'locationType.html', {'form': form})

#     else:
#         form = locationTypeForm()

#     return render(request, 'locationType.html', {'form': form})

def locationType(request):

	if request.method == 'POST':

		form = locationTypeForm(request.POST)
		

		print(form.data["description"])
		
		if(Locationtype.objects.filter(description = form.data["description"])):
			messages.error(request, 'Tipo de local já existe!')
		else:
			if form.is_valid():
				form.save() 
				messages.success(request, 'Tipo de local adicionado com sucesso!')
				return redirect('locationTypeList')

		# if a GET (or any other method) we'll create a blank form
			else:
				if form.errors.as_data().__contains__('name'):
					messages.error(request, 'O nome que tentou inserir já existe.')
				else:
					messages.error(request, 'Formulario inválido!')


	else:
		form = locationTypeForm()
	return render(request, 'locationType.html', {'form': form})

def locationTypeList(request):
	
	query = Locationtype.objects.all()

	print(query)
	
	return render(request, 'locationTypeList.html', {'query': query})



def locationTypeDelete(request, id):
	query = Locationtype.objects.get(id=id)
	query.delete()
	messages.success(request, 'Tipo de local eliminado com sucesso!')
	return redirect('locationTypeList')

def locationTypeEdit(request, id):
	obj = Locationtype.objects.get(id=id)
	if request.method == 'POST':
		form = locationTypeForm(request.POST, instance=obj)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			messages.success(request, 'Tipo de local editado com sucesso!')
			return redirect('locationTypeList')
		else:
			if form.errors.as_data().__contains__('name'):
				messages.error(request, 'O nome que tentou inserir já existe.')
			else:
				messages.error(request, 'Formulario inválido!')
	else:
		form = locationTypeForm(
		{
			'name' : str(obj.name),
			'description' : str(obj.description),		
		}
		)
	
	return render(request, 'locationTypeEdit.html', {'obj' : obj, 'form' : form})

def location(request):

	locationtypes = Locationtype.objects.all().values_list()

	campi = Campus.objects.all().values_list()


	# for loctype in locationtypes:
	#     print(loctype[1])

	if request.method == 'POST':

		form = locationForm(request.POST)
		
		# print(request.POST.get())

		loctype = request.POST.get("locationtype")
		campus = request.POST.get("campus")
		building = request.POST.get("building")
		maxcapacity = request.POST.get("maxcapacity")
		maxspecialneedscapacity = request.POST.get("maxspecialneedscapacity")
		
		
		# nao brinques



		novo = Campus.objects.get(id = campus)
		novo2 = Locationtype.objects.get(id = loctype)
		form.instance.name = request.POST.get("name")
		form.instance.campus = novo
		form.instance.locationtype = novo2
		form.instance.building = Building.objects.get(id=building)
		form.instance.maxcapacity = maxcapacity

		form.instance.maxspecialneedscapacity = maxspecialneedscapacity
		
		print("oi")
		
		print(form.instance.maxcapacity)
		print(form.instance.maxspecialneedscapacity)
		if form.instance.maxcapacity > form.instance.maxspecialneedscapacity:
			if form.is_valid():
				if(building is not None):
					obj = Location(name = form.instance.name, locationtype=form.instance.locationtype, building = form.instance.building ,campus = form.instance.campus, maxcapacity = form.instance.maxcapacity, maxspecialneedscapacity = form.instance.maxspecialneedscapacity)
					obj.save()
				else:	
					form.save()
				messages.success(request, 'Local adicionado com sucesso!')
				return redirect('locationList')
			else:
				messages.error(request, 'Formulario inválido!')
		else:
			messages.error(request, 'A lotação máxima tem de ser maior que a lotação para necessidades especiais.')

	else:
		form = locationForm()
	return render(request, 'location.html', {'form': form, 'locationtypes': locationtypes, 'campi' : campi})

def locationEdit(request, id):

	
	locationtypes = Locationtype.objects.all().values_list()
	
	campi = Campus.objects.all().values_list()
	
	obj = Location.objects.get(id=id)
	
  
	if request.method == 'POST':

		form = locationForm(request.POST, instance=obj)
		
		print("oi")
		print(form.instance.maxcapacity)
		
		loctype = request.POST.get("locationtype")
		campus = request.POST.get("campus")
		building = request.POST.get("building")

		form.instance.campus = Campus.objects.get(id = campus)
		form.instance.locationtype = Locationtype.objects.get(id = loctype)
		form.instance.building = Building.objects.get(id=building)

		

		if form.instance.maxcapacity > form.instance.maxspecialneedscapacity:
			if form.is_valid():
				if(building is not None):
					obj = form.save(commit=False)
					obj.save()

				messages.success(request, 'Local editado com sucesso!')
				return redirect('locationList')

			else:
				messages.error(request, 'Formulario inválido!')
		else:
			messages.error(request, 'A lotação máxima tem de ser maior que a lotação para necessidades especiais.')
	else:
		form = locationForm(
		{
			'name' : str(obj.name),
			'locationtype' : str(obj.locationtype),
			'building' : str(obj.building),
			'campus' : str(obj.campus),
			'maxcapacity' : str(obj.maxcapacity),
			'maxspecialneedscapacity' : str(obj.maxspecialneedscapacity),
			
		}
		)
	return render(request, 'locationEdit.html', {'form': form, 'locationtypes': locationtypes, 'campi' : campi, 'selected_id_loctype' : obj.locationtype.id, 'selected_id_campus' : obj.campus.id, 'selected_id_building' : obj.building.id})

def locationList(request):
	
	query = Location.objects.all()

	print(query)
	
	return render(request, 'locationList.html', {'query': query})

def locationDelete(request, id):
	query = Location.objects.get(id=id)
	query.delete()
	messages.success(request, 'Local eliminado com sucesso!')
	return redirect('locationList')

def servicesType(request):

	if request.method == 'POST':

		form = servicesTypeForm(request.POST)
		

		
		if(Servicestype.objects.filter(name = form.data["name"])):
			messages.error(request, 'Tipo de serviço já existe!')
		else:
			if form.is_valid():
				form.save() 
				messages.success(request, 'Tipo de serviços adicionado com sucesso!')
				return redirect('servicesTypeList')

		# if a GET (or any other method) we'll create a blank form
			else:
				if form.errors.as_data().__contains__('name'):
					messages.error(request, 'O nome que tentou inserir já existe.')
				else:
					messages.error(request, 'Formulario inválido!')

	else:
		form = servicesTypeForm()
	return render(request, 'servicesType.html', {'form': form})

def servicesTypeList(request):
	
	query = Servicestype.objects.all()

	print(query)
	
	return render(request, 'servicesTypeList.html', {'query': query})



def servicesTypeDelete(request, id):
	query = Servicestype.objects.get(id=id)
	query.delete()
	messages.success(request, 'Tipo de serviço eliminado com sucesso!')
	return redirect('servicesTypeList')

def servicesTypeEdit(request, id):
	obj = Servicestype.objects.get(id=id)
	if request.method == 'POST':
		form = servicesTypeForm(request.POST, instance=obj)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			messages.success(request, 'Tipo de serviços editado com sucesso!')
			return redirect('servicesTypeList')
		else:
			if form.errors.as_data().__contains__('name'):
				messages.error(request, 'O nome que tentou inserir já existe.')
			else:
				messages.error(request, 'Formulario inválido!')
	else:
		form = servicesTypeForm(
		{
			'name' : str(obj.name),
			'description' : str(obj.description)
		}
		)
	
	return render(request, 'servicesTypeEdit.html', {'obj' : obj, 'form' : form})


# def requestEquipment(request, equipmentId, eventId):

#     equipment = Typeequipment.objects.all().values_list()

#     events = Event.objects.all().values_list()

#     # for loctype in locationtypes:
#     #     print(loctype[1])

#     if request.method == 'POST':

#         form = locationFbuildingorm(request.POST)
		
#         # print(request.POST.get())

#         loctype = request.POST.get("locationtype")
#         campus = request.POST.get("campus")

#         print(campus)

#         novo = Campus.objects.get(id = campus)
#         novo2 = Locationtype.objects.get(id = loctype)

#         form.instance.campus = novo
#         form.instance.locationtype = novo2
#         if form.is_valid():
#             building = request.POST.get("building")
#             if(building is not None):
#                 obj = Location(name = form.instance.name, locationtype=form.instance.locationtype, building = building,campus = form.instance.campus, maxcapacity = form.instance.maxcapacity, maxspecialneedscapacity = form.instance.maxspecialneedscapacity)
#                 obj.save()
#             else:   
			
#                 form.save()
			
			
#             messages.success(request, 'Tipo de local adicionado com sucesso!')
#             return render(request, 'location.html', {'form': form, 'locationtypes': locationtypes, 'campi' : campi})

#         else:
#             messages.error(request, 'Formulario inválido!')

#     else:
#         form = locationForm()
#     return render(request, 'location.html', {'form': form, 'locationtypes': locationtypes, 'campi' : campi})

def campusAdd(request):

	if request.method == 'POST':

		form = campusForm(request.POST)
				
		if(Campus.objects.filter(name = form.data["name"])):
			messages.error(request, 'Campus já existe!')
		else:
			if form.is_valid():
				form.save() 
				messages.success(request, 'Campus adicionado com sucesso!')
				return redirect('campusList')

			else:
				if form.errors.as_data().__contains__('name'):
					messages.error(request, 'O nome que tentou inserir já existe.')
				else:
					messages.error(request, 'Formulario inválido!')

	else:
		form = campusForm()
	return render(request, 'campus.html', {'form': form})


def campusList(request):
	
	query = Campus.objects.all()

	print(query)
	
	return render(request, 'campusList.html', {'query': query})



def campusDelete(request, id):
	query = Campus.objects.get(id=id)
	query.delete() 
	messages.success(request, 'Campus eliminado com sucesso!')
	return redirect('campusList')

def campusEdit(request, id):
	obj = Campus.objects.get(id=id)
	if request.method == 'POST':
		form = campusForm(request.POST, instance=obj)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			messages.success(request, 'Campus editado com sucesso!')
			return redirect('campusList')
		else:
			if form.errors.as_data().__contains__('name'):
				messages.error(request, 'O nome que tentou inserir já existe.')
			else:
				messages.error(request, 'Formulario inválido!')
	else:
		form = campusForm(
		{
			'name' : str(obj.name),
		}
		)
	
	return render(request, 'campusEdit.html', {'obj' : obj, 'form' : form})



def buildingAdd(request):
	campi = Campus.objects.all().values_list()
	
	if request.method == 'POST':

		form = buildingForm(request.POST)
				
		campus = request.POST.get("campus")

		print(campus)
		
		form.instance.campus = Campus.objects.get(id=campus)
		if form.is_valid():
			form.save() 
			messages.success(request, 'Edificio adicionado com sucesso!')
			return redirect('buildingList')

		else:
			messages.error(request, 'Formulario inválido!')

	else:
		form = buildingForm()
	return render(request, 'building.html', {'form': form, 'campi': campi})


def buildingList(request):
	
	query = Building.objects.all()

	print(query)
	
	return render(request, 'buildingList.html', {'query': query})



def buildingDelete(request, id):
	query = Building.objects.get(id=id)
	query.delete()
	messages.success(request, 'Edificio eliminado com sucesso!')
	return redirect('buildingList')

def buildingEdit(request, id):
	campi = Campus.objects.all().values_list()
	obj = Building.objects.get(id=id)
	if request.method == 'POST':
		form = buildingForm(request.POST, instance=obj)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			messages.success(request, 'Edificio editado com sucesso!')  
			return redirect('buildingList')
		else:
			messages.error(request, 'Formulario inválido!')
	else:
		form = buildingForm(
		{
			'name' : str(obj.name),
			'campus' : obj.campus.id,
		}
		)
	
	return render(request, 'buildingEdit.html', {'obj' : obj, 'form' : form, 'campi': campi, 'selected_id' : obj.campus.id })


# def roomAdd(request):

#     campi = Campus.objects.all().values_list()

#     if request.method == 'POST':

#         form = roomForm(request.POST)
		
#         building = request.POST.get("building")

#         form.instance.building = Building.objects.get(id=building)

#         if form.is_valid():
			
#             form.save()
#             messages.success(request, 'Sala adicionada com sucesso!')
#             return redirect('roomList')

#         else:
#             messages.error(request, 'Formulario inválido!')

#     else:
#         form = roomForm()
#     return render(request, 'room.html', {'form': form, 'campi' : campi})


# def roomList(request):
	
#     query = Room.objects.all()

#     print(query)
	
#     return render(request, 'roomList.html', {'query': query})



# def roomDelete(request, id):
#     query = Building.objects.get(id=id)
#     query.delete()
#     messages.success(request, 'Edificio eliminado com sucesso!')
#     return redirect('buildingList')

# def roomEdit(request, id):
#     campi = Campus.objects.all().values_list()
#     obj = Building.objects.get(id=id)
#     if request.method == 'POST':
#         form = buildingForm(request.POST, instance=obj)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.save()
#             messages.success(request, 'Edificio editado com sucesso!')  
#             return redirect('buildingList')
#         else:
#             messages.error(request, 'Formulario inválido!')
#     else:
#         form = buildingForm()
	
#     return render(request, 'buildingEdit.html', {'obj' : obj, 'form' : form, 'campi': campi})


def campusView(request, id):
	obj= Campus.objects.get(id=id)
	return render(request, 'campusView.html', {'obj': obj})

def buildingView(request, id):
	obj= Building.objects.get(id=id)
	return render(request, 'buildingView.html', {'obj': obj})

def equipmentView(request, id):
	obj= Typeequipment.objects.get(id=id)
	return render(request, 'equipmentView.html', {'obj': obj})

def itemView(request, id):
	obj= Item.objects.get(id=id)
	return render(request, 'itemView.html', {'obj': obj})

def locationView(request, id):
	obj= Location.objects.get(id=id)
	return render(request, 'locationView.html', {'obj': obj})

def locationTypeView(request, id):
	obj= Locationtype.objects.get(id=id)
	return render(request, 'locationTypeView.html', {'obj': obj})

def serviceView(request, id):
	obj= Service.objects.get(id=id)
	return render(request, 'serviceView.html', {'obj': obj})

def servicesTypeView(request, id):
	obj= Servicestype.objects.get(id=id)
	return render(request, 'servicesTypeView.html', {'obj': obj})

def itemAdd(request):
	equipmenttypes = Typeequipment.objects.all().values_list()
	
	if request.method == 'POST':

		form = itemForm(request.POST)

		print(form.data)
				
		equipmenttype = request.POST.get("equipmenttype")

		print(equipmenttype)

		# print(Typeequipment.objects.get(id=equipmenttype).name)
		
		form.instance.typeequipment = Typeequipment.objects.get(id=equipmenttype)
		print(form.instance.typeequipment.name)
		if form.is_valid():
			form.save() 
			messages.success(request, 'Equipamento adicionado com sucesso!')
			return redirect('itemList')

		else:

			print(form.errors)
			if form.errors.as_data().__contains__('name'):
				messages.error(request, 'O nome que tentou inserir já existe.')
			else:
				messages.error(request, 'Formulario inválido!')

	else:
		form = itemForm()
	return render(request, 'itemAdd.html', {'form': form, 'equipmenttypes': equipmenttypes})

def itemList(request):
	
	query = Item.objects.all()

	print(query)
	
	return render(request, 'itemList.html', {'query': query})



def itemDelete(request, id):
	query = Item.objects.get(id=id)
	query.delete() 
	messages.success(request, 'Equipamento eliminado com sucesso!')
	return redirect('itemList')

def itemEdit(request, id):
	equipmenttypes = Typeequipment.objects.all().values_list()
	obj = Item.objects.get(id=id)
	if request.method == 'POST':
		form = itemForm(request.POST, instance=obj)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			messages.success(request, 'Equipamento editado com sucesso!')  
			return redirect('itemList')
		else:
			if form.errors.as_data().__contains__('name'):
				messages.error(request, 'O nome que tentou inserir já existe.')
			else:
				messages.error(request, 'Formulario inválido!')
	else:
		form = itemForm(
		{
			'typeequipment' : str(obj.typeequipment.id),
			'name' : str(obj.name),
			'serialnum' : str(obj.serialnum),
		}
		)
	
	return render(request, 'itemEdit.html', {'obj' : obj, 'form' : form, 'equipmenttypes': equipmenttypes, 'selected_id' : obj.typeequipment.id})



def serviceAdd(request):
	servicestypes = Servicestype.objects.all().values_list()
	
	if request.method == 'POST':

		form = serviceForm(request.POST)

		print(form.data)
				
		servicesType = request.POST.get("servicestype")

		form.instance.servicestype = Servicestype.objects.get(id=servicesType)

		if form.is_valid():
			form.save() 
			messages.success(request, 'Serviço adicionado com sucesso!')
			return redirect('serviceList')

		else:
			if form.errors.as_data().__contains__('name'):
				messages.error(request, 'O nome que tentou inserir já existe.')
			else:
				messages.error(request, 'Formulario inválido!')

	else:
		form = serviceForm()
	return render(request, 'serviceAdd.html', {'form': form, 'servicestypes': servicestypes})

def serviceList(request):
	
	query = Service.objects.all()

	print(query)
	
	return render(request, 'serviceList.html', {'query': query})



def serviceDelete(request, id):
	query = Service.objects.get(id=id)
	query.delete() 
	messages.success(request, 'Serviço eliminado com sucesso!')
	return redirect('serviceList')

def serviceEdit(request, id):
	servicestypes = Servicestype.objects.all().values_list()
	obj = Service.objects.get(id=id)
	if request.method == 'POST':
		form = serviceForm(request.POST, instance=obj)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			messages.success(request, 'Serviço editado com sucesso!')  
			return redirect('serviceList')
		else:
			if form.errors.as_data().__contains__('name'):
				messages.error(request, 'O nome que tentou inserir já existe.')
			else:
				messages.error(request, 'Formulario inválido!')
	else:
		form = serviceForm(
		{
			'name' : str(obj.name),
			'description' : str(obj.description),
			'servicestype' : str(obj.servicestype.id),
		}
		)
	
	return render(request, 'serviceEdit.html', {'obj' : obj, 'form' : form, 'servicestypes': servicestypes, 'selected_id' : obj.servicestype.id})



def list_buildings(request):
	buildings = Building.objects.filter(campus=request.GET["campus"])
	print(request.GET["campus"])
	print({b.id: b.name for b in buildings})
	return JsonResponse({b.id: b.name for b in buildings}, safe=False)
