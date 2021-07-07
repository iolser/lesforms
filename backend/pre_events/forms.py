from django import forms
from django.forms.models import modelformset_factory

from resources.models import Event, Eventtype, Requestequipment, Requestlocation, Requestservices, Itemuse, Serviceuse, Locationuse


resource_groups = [
	("services", "Tipos de serviço"),
	("equipment", "Tipos de equipamento"),
	("location" , "Tipos de espaço")
]

groups = Eventtype.objects.all()

eventtype_dict = {}

for group in groups:
	key = str(group.pk)
	value = str(group.name)
	eventtype_dict[key] = value

eventtype_choices = [(k, v) for k, v in eventtype_dict.items()]

class EventLogisticsForm(forms.Form):
	resource_type = forms.CharField(label="Selecione o recurso que pretende adicionar",
									widget=forms.Select(choices=resource_groups))

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ["name", "description", "eventtype", "start", "end", "state"]
		excluded = ('state',)
		widgets = {
			"name" : forms.TextInput(attrs={ 'class':'input' }),
			"description": forms.Textarea(attrs={ 'class':'textarea' }),
			"eventtype": forms.Select(choices=eventtype_choices),
			"start": forms.DateTimeInput(attrs={ 'class':'input', 'type':'datetime-local' }),
			"end": forms.DateTimeInput(attrs={ 'class':'input', 'type':'datetime-local' }),
			"state": forms.HiddenInput(attrs={'value':'0'})
		}

class RequestEquipmentForm(forms.ModelForm):
	class Meta:
		model = Requestequipment
		fields = ["typeequipment", "start", "end", "quantity"]
		widgets = {
			"typeequipment" : forms.Select(attrs={
				'class': 'select is-info',
			}),
            "start" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
            "end" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
			"quantity" : forms.NumberInput(attrs={
				"class": "input",
               "min":"1",
               "max":"99"
            }),
		}

class RequestLocationForm(forms.ModelForm):
	class Meta:
		model = Requestlocation
		fields = ["locationtype", "start", "end", "quantity"]
		widgets = {
			"locationtype" : forms.Select(attrs={
				'class': 'select is-info',
			}),
            "start" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
            "end" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
			"quantity" : forms.NumberInput(attrs={
				"class": "input",
           		"min":"1",
            	"max":"99"
            }),
		}

class RequestServicesForm(forms.ModelForm):
	class Meta:
		model = Requestservices
		fields = ["servicestype", "start", "end", "quantity"]
		widgets = {
			"servicestype" : forms.Select(attrs={
				'class': 'select is-info',
			}),
            "start" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
            "end" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
            "quantity" : forms.NumberInput(attrs={
				"class": "input",
               	"min":"1",
               	"max":"99"
            }),
		}

class ItemuseForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Itemuse
        fields = ["start", "end"]
        widgets = {
            "start" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
            "end" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
        }

class ServiceuseForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Serviceuse
        fields = ["start", "end"]
        widgets = {
            "start" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
            "end" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
		}

class LocationuseForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Locationuse
        fields = ["start", "end"]
        widgets = {
            "start" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
            "end" : forms.DateTimeInput(attrs={
				'class': 'input',
				'type': 'datetime-local'
			}),
		}

RequestServicesFormset = modelformset_factory(model=Requestservices, form=RequestServicesForm, fields=("servicestype", "start", "end", "quantity"), can_delete=True)
RequestEquipmentFormset = modelformset_factory(model=Requestequipment, form=RequestEquipmentForm, fields=("typeequipment", "start", "end", "quantity"), can_delete=True)
RequestLocationFormset = modelformset_factory(model=Requestlocation, form=RequestLocationForm, fields=("locationtype", "start", "end", "quantity"), can_delete=True)

