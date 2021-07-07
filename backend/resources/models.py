# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.contrib.auth.models import Group
from django.conf import settings


from forms.models import Form, FormAnswer, FormType

class Generaluser(models.Model):
	user_ptr = models.OneToOneField(settings.AUTH_USER_MODEL, models.DO_NOTHING, primary_key=True)
	contact = models.CharField(max_length=20)

class Participant(models.Model):
	generaluser_ptr = models.OneToOneField(Generaluser, models.DO_NOTHING, primary_key=True)

class Proponent(models.Model):
	generaluser_ptr = models.OneToOneField(Generaluser, models.DO_NOTHING, primary_key=True)

class Administrator(models.Model):
	generaluser_ptr = models.OneToOneField(Generaluser, models.DO_NOTHING, primary_key=True)
	gabinete = models.CharField(max_length=255)

class Event(models.Model):
	eventtype = models.ForeignKey('Eventtype', models.DO_NOTHING)   # Field name made lowercase.
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=256, blank=True, null=True)
	organizer = models.ForeignKey('Proponent', models.DO_NOTHING,  null=True)
	state = models.IntegerField()
	start = models.DateTimeField()
	end = models.DateTimeField(blank=True, null=True)
	formsignupid = models.ForeignKey(Form, on_delete=models.SET_NULL, blank=True, null=True, related_name='events_signup')  # Field name made lowercase.
	formfeedbackid = models.ForeignKey(Form, on_delete=models.SET_NULL, blank=True, null=True, related_name='events_feedback')  # Field name made lowercase.

	def __str__(self):
		return self.name
	# class Meta:
		# db_table = 'event'
		# unique_together = (('id', 'eventtype'),)


class Eventtype(models.Model):
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=256, blank=True, null=True)
	formsignupid = models.ForeignKey(Form, related_name='type_signup', on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
	formfeedbackid = models.ForeignKey(Form, related_name='type_feedback', on_delete=models.SET_NULL, null=True)  # Field name made lowercase.
	formproposalid = models.ForeignKey(Form, related_name='type_proposal', on_delete=models.SET_NULL, null=True)  # Field name made lowercase.

	def __str__(self):
		return self.name

class Feedback(models.Model):
	feedbackdate = models.DateTimeField( blank=True, null=True)  # Field name made lowercase.
	event = models.ForeignKey(Event, models.DO_NOTHING,  blank=True, null=True)
	user = models.ForeignKey('Participant', models.DO_NOTHING,  blank=True, null=True)

class Item(models.Model):
	typeequipment = models.ForeignKey('Typeequipment', models.DO_NOTHING)   # Field name made lowercase.
	name = models.CharField(max_length=32, unique=True)
	serialnum = models.CharField( max_length=32)  # Field name made lowercase.

	def __str__(self):
		return self.name

class Itemuse(models.Model):
	item = models.ForeignKey(Item, models.DO_NOTHING,  blank=True, null=True)
	event = models.ForeignKey(Event, on_delete=models.CASCADE,  blank=True, null=True)
	start = models.DateTimeField()
	end = models.DateTimeField()

class Location(models.Model):
	name = models.CharField(max_length=32)
	locationtype = models.ForeignKey('Locationtype', models.DO_NOTHING,  blank=False, null=False)  # Field name made lowercase.
	building = models.ForeignKey('Building', models.DO_NOTHING,  blank=False)
	campus = models.ForeignKey('Campus', models.DO_NOTHING,  blank=False)
	maxcapacity = models.IntegerField( blank=False, null=False)  # Field name made lowercase.
	maxspecialneedscapacity = models.IntegerField( blank=False, null=False)  # Field name made lowercase.

	def __str__(self):
		return self.name

class Campus(models.Model):
	name = models.CharField(max_length=128, blank=False, null=True, unique=True)

	def __str__(self):
		return self.name

class Building(models.Model):
	name = models.CharField(max_length=128, blank=False, null=False, unique=False)
	campus = models.ForeignKey('Campus', models.DO_NOTHING,  blank=False, null=False)

	def __str__(self):
		return self.name

class Locationtype(models.Model):
	name = models.CharField(max_length=32, unique=True)
	description = models.CharField(max_length=1024, blank=True, null=True)

	def __str__(self):
		return self.name

class Locationuse(models.Model):
	location = models.ForeignKey(Location, models.DO_NOTHING,  blank=True, null=True)
	event = models.ForeignKey(Event, on_delete=models.CASCADE,  blank=True, null=True)
	start = models.DateTimeField()
	end = models.DateTimeField()

class Register(models.Model):
	registerdate = models.DateTimeField( blank=True, null=True)  # Field name made lowercase.
	event = models.ForeignKey(Event, on_delete=models.CASCADE,  blank=True, null=True)
	user = models.ForeignKey(Participant, models.DO_NOTHING,  blank=True, null=True)

class Requestequipment(models.Model):
	typeequipment = models.ForeignKey('Typeequipment', models.DO_NOTHING, blank=True, null=True)
	quantity = models.IntegerField(blank=False, null=False, default=1)
	additionalinfo = models.CharField( max_length=128)  # Field name made lowercase.
	valid = models.BooleanField(default=False)
	start = models.DateTimeField()
	end = models.DateTimeField()
	event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Requestlocation(models.Model):
	locationtype = models.ForeignKey('Locationtype', models.DO_NOTHING,  blank=True, null=True)  # Field name made lowercase.
	quantity = models.IntegerField(blank=False, null=False, default=1)
	additionalinfo = models.CharField( max_length=128)  # Field name made lowercase.
	valid = models.BooleanField(default=False)
	start = models.DateTimeField()
	end = models.DateTimeField()
	event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Requestservices(models.Model):
	servicestype = models.ForeignKey('Servicestype', models.DO_NOTHING,  blank=True, null=True)  # Field name made lowercase.
	quantity = models.IntegerField(blank=False, null=False, default=1)
	additionalinfo = models.CharField( max_length=128)  # Field name made lowercase.
	valid = models.BooleanField(default=False)
	start = models.DateTimeField()
	end = models.DateTimeField()
	event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Serviceuse(models.Model):
	service = models.ForeignKey('Service', models.DO_NOTHING, default=None)  # Field name made lowercase.
	event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
	start = models.DateTimeField()
	end = models.DateTimeField()


class Service(models.Model):
	name = models.CharField(max_length=128, unique=True)
	description = models.CharField(max_length=1024, blank=True, null=True)
	servicestype = models.ForeignKey('Servicestype', models.DO_NOTHING,  blank=False, null=False)

	def __str__(self):
		return self.name

class Servicestype(models.Model):
	name = models.CharField(max_length=126, blank=True, null=True, unique=True)
	description = models.CharField(max_length=126, blank=True, null=True)

	def __str__(self):
		return self.name

class Typeequipment(models.Model):
	name = models.CharField(max_length=32, unique=True)
	image = models.CharField(max_length=128, blank=True, null=True)

	def __str__(self):
		return self.name