from django.db import models
from django.conf import settings

# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from colorfield.fields import ColorField

from django.core import serializers

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class FormType(models.Model):
	name = models.CharField(max_length=32, blank=False, null=False)
	description = models.CharField(max_length=256, blank=True, null=True)
	color = ColorField(default='#DDDDDD')

	class Meta:
		db_table = 'formType'

	def __str__(self):
		return self.name

class AnswerStatus(models.Model):
	name = models.CharField(max_length=256, blank=False)
	color = ColorField(default='#DDDDDD')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Answer statuses"

class Form(models.Model):
	title = models.CharField(max_length=256, blank=False)
	form = models.JSONField(blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	submit_message = models.TextField(blank=False, null=False, default="Resposta submetida com sucesso!")
	redirect = models.CharField(max_length=256, blank=False, null=False, default="pre_events/consult_events")
	redirect_delay = models.PositiveIntegerField(blank=False, null=False, default=3)
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='forms', null=True, on_delete=models.SET_NULL)
	type = models.ForeignKey(FormType, related_name='forms', on_delete=models.PROTECT, null=True)
	category = models.ForeignKey('resources.eventtype', related_name='forms', on_delete=models.SET_NULL, null=True)
	editable = models.BooleanField(default=True)
	hidden = models.BooleanField(default=True)

	def __str__(self):
		return self.title

from django.contrib.auth.models import User
import secrets
class FormAnswer(models.Model):
	def authentication_key_default():
		return secrets.token_urlsafe(16)

	form = models.ForeignKey(Form, related_name='answers', blank=False, null=False, on_delete=models.CASCADE)
	content = models.JSONField(blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	event = models.ForeignKey("resources.Event", related_name='formAnswers', null=True, on_delete=models.CASCADE)
	answerer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answeredForms', null=True, on_delete=models.SET_NULL)
	editor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='editedForms', null=True, on_delete=models.SET_NULL)
	status = models.ForeignKey(AnswerStatus, default="1", on_delete=models.PROTECT)
	authentication_key = models.CharField(max_length=32, blank=False, null=False, default=authentication_key_default)

	def __str__(self):
		user = self.answerer
		if user is None:
			username = "Anónimo"
		else:
			username = user.username
		return "Resposta de " + username + " a " + self.form.title

	class Meta:
		permissions = [
			("update_status", "Can update submission status"),
			("request_auth", "Can request an authentication_key"),
		]

class Certificate(models.Model):
	event = models.OneToOneField("resources.Event", related_name='certificate', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	title = models.CharField(max_length=128, blank=False, null=False)
	subtitle = models.CharField(max_length=128, blank=False, null=False)
	text = models.CharField(max_length=256, blank=False, null=False)
	date = models.CharField(max_length=128, blank=True, null=True)
	signature1 = models.CharField(max_length=64, blank=True, null=True)
	signature2 = models.CharField(max_length=64, blank=True, null=True)
	signatureImage1 = models.ImageField(upload_to='signatures', blank=True, null=True)
	signatureImage2 = models.ImageField(upload_to='signatures', blank=True, null=True)

	available = models.BooleanField(default=False)

	def __str__(self):
		return "Certificado de " + self.event.name

class Ticket(models.Model):
	event = models.OneToOneField("resources.Event", related_name='ticket', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	start = models.CharField(max_length=128, blank=True, null=True)
	end = models.CharField(max_length=128, blank=True, null=True)
	location = models.CharField(max_length=128, blank=False, null=False)
	emergencyContact1 = models.CharField(max_length=128, blank=True, null=True)
	emergencyContact2 = models.CharField(max_length=128, blank=True, null=True)

	available = models.BooleanField(default=False)

	def __str__(self):
		return "Bilhete de " + self.event.name