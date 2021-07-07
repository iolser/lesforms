from rest_framework import serializers
from .models import Form, FormAnswer, AnswerStatus, FormType, Certificate, Ticket
from resources.models import Event, Eventtype

from forms.schema.FormsSchema import schema as forms_schema
from forms.schema.FormsValidator import FormsValidator

from forms.schema.AnswersSchema import schema as answers_schema

from rest_framework.exceptions import APIException

from forms.validators.FieldValidator import FieldValidator
from cerberus import Validator

from django.contrib.auth.models import User

import json

class FormTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = FormType
		exclude = []

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		exclude = []
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'groups']

class EventSerializer(serializers.ModelSerializer):
	signup_responses = serializers.IntegerField(read_only=True)
	feedback_responses = serializers.IntegerField(read_only=True)
	ticket_available = serializers.BooleanField(source="ticket.available", read_only=True)
	certificate_available = serializers.BooleanField(source="certificate.available", read_only=True)

	class Meta:
		model = Event
		exclude = []

class SimpleEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		exclude = []

class CertificateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Certificate
		exclude = []

class CheckinSerializer(serializers.ModelSerializer):
	author_first_name = serializers.CharField(source='answerer.first_name', read_only=True)
	author_last_name = serializers.CharField(source='answerer.last_name', read_only=True)
	event_name = serializers.CharField(source='event.name', read_only=True)
	event_start = serializers.DateTimeField(source='event.start', read_only=True)
	event_end = serializers.DateTimeField(source='event.end', read_only=True)
	class Meta:
		model = FormAnswer
		fields = [
			#Author
			'author_first_name', 
			'author_last_name',
			#Answer
			'id',
			'status', 
			'authentication_key',
			# Event
			'event_name', 
			'event_start', 
			'event_end']

class TicketSerializer(serializers.ModelSerializer):
	event_name = serializers.CharField(source='event.name', read_only=True)

	class Meta:
		model = Ticket
		exclude = []

class EventTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Eventtype
		exclude = []

class AnswerStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = AnswerStatus
		exclude = []

class FormAnswerStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = FormAnswer
		fields = ['id', 'status']
    
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'groups']

class FormListSerializer(serializers.ModelSerializer):
	responses = serializers.IntegerField(read_only=True)
	signup_uses = serializers.IntegerField(read_only=True)
	feedback_uses = serializers.IntegerField(read_only=True)
	class Meta:
		model = Form
		fields = ['id', 'title', 'type', 'responses', 'signup_uses', 'feedback_uses', 'category', 'hidden']

class FormSerializer(serializers.ModelSerializer):
	responses = serializers.ReadOnlyField(read_only=True)
	signup_uses = serializers.IntegerField(read_only=True)
	feedback_uses = serializers.IntegerField(read_only=True)
	class Meta:
		model = Form
		exclude = []

	def validate(self, data):
		if ('form' in data) :
			v = FormsValidator(forms_schema)
			if not v.validate(data['form']):
				raise serializers.ValidationError({"error" : "Invalid form", "detail" : v.errors})
			data['form'] = v.normalized(data['form'])
		return data

class FormEditSerializer(serializers.ModelSerializer):
	class Meta:
		model = Form
		fields = ['id', 'title', 'submit_message', 'redirect', 'redirect_delay', 'category', 'type', 'hidden']

class FormAnswerAuthorSerializer(serializers.ModelSerializer):
	author_first_name = serializers.CharField(source='answerer.first_name', read_only=True)
	author_last_name = serializers.CharField(source='answerer.last_name', read_only=True)
	class Meta:
		model = FormAnswer
		fields = ['event', 'author_first_name', 'author_last_name']

class FormAnswerAuthorNoAuthSerializer(serializers.ModelSerializer):
	author_first_name = serializers.CharField(source='answerer.first_name', read_only=True)
	author_last_name = serializers.CharField(source='answerer.last_name', read_only=True)
	class Meta:
		model = FormAnswer
		fields = ['id', 'author_first_name', 'author_last_name', 'authentication_key']

class FormAnswerAuthorListSerializer(serializers.ModelSerializer):
	author_first_name = serializers.CharField(source='answerer.first_name', read_only=True)
	author_last_name = serializers.CharField(source='answerer.last_name', read_only=True)
	class Meta:
		model = FormAnswer
		fields = ['author_first_name', 'author_last_name']

class FormAnswerSerializer(serializers.ModelSerializer):
	author = serializers.CharField(source='answerer.username', read_only=True)
	editor = serializers.CharField(source='editor.username', read_only=True)
	eventName = serializers.CharField(source='event.name', read_only=True)
	certificateAvailable = serializers.BooleanField(source='event.certificate.available', read_only=True)
	ticketAvailable = serializers.BooleanField(source='event.ticket.available', read_only=True)
	feedbackForm = serializers.IntegerField(source='event.formfeedbackid.id', read_only=True)

	class Meta:
		model = FormAnswer
		exclude = ['authentication_key']

	def validate(self, data):
		answerValidator = Validator(answers_schema)
		if not answerValidator.validate(data['content']):
			raise serializers.ValidationError({"error" : "Invalid answer", "detail" : answerValidator.errors})

		formValidator = FormsValidator(forms_schema)
		if not formValidator.validate(data['form'].form):
			raise serializers.ValidationError({"error" : "Invalid form", "detail" : formValidator.errors})

		if len(formValidator.document["sections"]) != len(answerValidator.document["sections"]):
			raise serializers.ValidationError({"error" : "Incompatible amount of sections for the form."})
		for sa, sb in zip(formValidator.document["sections"], answerValidator.document["sections"]):
			if len(sa["questions"]) != len(sb):
				raise serializers.ValidationError({"error" : "Incompatible amount of answers for the section."})
			for qa, qb in zip(sa["questions"], sb):
				if qa["properties"]["field_type"] != qb["field_type"]:
					raise serializers.ValidationError(
						{"error" : "Incompatible answer type", 
						"detail" : "The answer format({}) does not match the question format({}).".format(qa["properties"]["field_type"], qb["field_type"])})
				if not "answer" in qb or (isinstance(qb["answer"], list) and not qb["answer"]):
					if qa["required"] is True:
						raise serializers.ValidationError({"error" : "Required {} field '{}' is empty.".format(qa["properties"]["field_type"], qa["question"])})
				else:
					FieldValidator.validateField(qb["answer"], qa["properties"])
		data['content'] = answerValidator.normalized(data['content'])
		return data