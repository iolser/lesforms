from django import forms
from .models import *

# class equipmentForm(forms.Form):
#     equipmentName = forms.CharField(label='Equipment name', max_length=100)
#     imageURL = forms.CharField(max_length=100, required=False)

# class locationTypeForm(forms.Form):
#     locationName = forms.CharField(label='locationType name', max_length=100, required=True)
#     maxCapacity = forms.IntegerField( required=True)
#     maxSpecialNeedsCapacity = forms.IntegerField( required=True)

class equipmentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Typeequipment
        fields = ["name"]
        widgets = {
            "name" : forms.TextInput(attrs={'class':'input'}),
        }


class locationTypeForm(forms.ModelForm):
    class Meta:
        model = Locationtype
        fields = ["name", "description"]
        widgets = {
            "name" : forms.TextInput(attrs={'class':'input'}),
			"description" : forms.Textarea(attrs={'class':'textarea'})
        }

class itemForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Item
        fields = ["name", "serialnum"]
        widgets = {
            "name" : forms.TextInput(attrs={'class':'input'}),
			"serialnum" : forms.TextInput(attrs={'class':'input'}),
        }

class locationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "locationtype", "building", "campus", "maxcapacity", "maxspecialneedscapacity"]
        widgets = {
            "name" : forms.TextInput(attrs={'class':'input'}),
            # "locationtype" : forms.IntegerField(),
            "building" : forms.TextInput(attrs={'class':'input'}),
            # "campus" : forms.IntegerField(),
            "maxcapacity" : forms.TextInput(attrs={'class':'input',
			'type' : 'number'}),
            "maxspecialneedscapacity" : forms.TextInput(attrs={'class':'input',
			'type' : 'number'}),
        }


class serviceForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Service
        fields = ["name", "description"]
        widgets = {
            "name" : forms.TextInput(attrs={'class':'input'}),
            "description" : forms.Textarea(attrs={'class':'textarea'}),
        }



class servicesTypeForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Servicestype
        fields = ["name", "description"]
        widgets = {
            "name" : forms.TextInput(attrs={'class':'input'}),
            "description" : forms.Textarea(attrs={'class':'textarea'}),
        }


class campusForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Campus
        fields = ["name"]
        widgets = {
            "name" : forms.TextInput(attrs={'class':'input'}),
        }

class buildingForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Building
        fields = ["name", "campus"]
        widgets = {
            "name" : forms.TextInput(attrs={'class':'input'}),
        }

# class roomForm(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = Room
#         fields = ["name", "building"]
#         widgets = {
#             "name" : forms.TextInput(attrs={'class':'input'}),
#         }
# class requestEquipmentForm(forms.ModelForm):
#     class Meta:
#         model = Requestequipment
#         fields = ["Typeequipment", "Additionalinfo", "start", "end", "event"]
#         widgets = {
#             # "typeequipment" : 
#             "additionalinfo" : forms.Textarea(attrs={'class':'textarea'}),
#             # "start" : forms.Date  TimeField(auto_now=True),
#             # "end" : forms.DateTimeInput(auto_now=True),
#             # "event" : forms.InlineForeignKeyField()
#         }