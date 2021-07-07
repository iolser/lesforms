from django.shortcuts import render

from .models import Form, FormAnswer, AnswerStatus, FormType, Certificate, Ticket
from resources.models import Event, Eventtype
from .serializers import *
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser

from django.contrib.auth.models import User

# Create your views here.

class UserInfoView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserInfoSerializer

from django.db.models import Case, Count, When, IntegerField

class MyEventView(viewsets.ModelViewSet):
	queryset = FormAnswer.objects.all()
	serializer_class = FormAnswerSerializer

	def get_queryset(self):
		queryset = FormAnswer.objects.prefetch_related('event') \
		.prefetch_related('answerer').prefetch_related('editor') \
		.prefetch_related('form').prefetch_related('event__certificate').prefetch_related('event__ticket')
		user = self.request.user
		if not self.request.user.is_anonymous:
			queryset = queryset.filter(answerer=user)
		else:
			queryset = queryset.none()

		type = self.request.query_params.get('type', None)
		if type is not None:
			type = type.split(',')
			queryset = queryset.filter(form__type__in=type)
		return queryset

class EventView(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer

	def get_queryset(self):
		queryset = Event.objects.all() \
		.prefetch_related("formAnswers") \
		.annotate(signup_responses=Count(
			Case(
					When(formAnswers__form__type=1, then=1)
				), 
				output_field=IntegerField()
			)
		) \
		.annotate(feedback_responses=Count(
			Case(
					When(formAnswers__form__type=3, then=1)
				), 
				output_field=IntegerField()
			)
		)
		return queryset

class CheckinView(viewsets.ModelViewSet):
	queryset = FormAnswer.objects.prefetch_related('answerer').prefetch_related('event').all()
	serializer_class = CheckinSerializer

class FormAnswerAuthorView(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	queryset = FormAnswer.objects.prefetch_related("author").all()
	serializer_class = FormAnswerAuthorSerializer

	def get_serializer_class(self):
		if (self.action=='list'):
			return FormAnswerAuthorListSerializer
		return self.serializer_class

	def get_queryset(self):
		queryset = FormAnswer.objects.filter(status=4, event__certificate__available=True)
		auth = self.request.query_params.get('auth', None)
		if auth is not None:
			queryset = queryset.filter(authentication_key=auth)
		else:
			queryset = queryset.none()
		return queryset

class FormAnswerAuthorNoAuthView(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	queryset = FormAnswer.objects.prefetch_related("author").all()
	serializer_class = FormAnswerAuthorNoAuthSerializer

	def get_queryset(self):
		queryset = FormAnswer.objects
		form = self.request.query_params.get('form', None)
		event = self.request.query_params.get('event', None)
		status = self.request.query_params.get('status', None)
		user = self.request.user
		if form is not None:
			queryset = queryset.filter(form=form)
		if event is not None:
			queryset = queryset.filter(event=event)
		if status is not None:
			status = status.split(',')
			queryset = queryset.filter(status__in=status)
		if not self.request.user.is_anonymous:
			queryset = queryset.filter(answerer=user)
		else:
			queryset = queryset.none()
		return queryset

class CertificateView(viewsets.ModelViewSet):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer

	def get_queryset(self):
		queryset = Certificate.objects
		event = self.request.query_params.get('event', None)
		if event is not None:
			queryset = queryset.filter(event=event)
		return queryset

class TicketView(viewsets.ModelViewSet):
	queryset = Ticket.objects.prefetch_related('event').all()
	serializer_class = TicketSerializer

	def get_queryset(self):
		queryset = Ticket.objects.prefetch_related('event')
		event = self.request.query_params.get('event', None)
		if event is not None:
			queryset = queryset.filter(event=event)
		return queryset

class EventTypeView(viewsets.ModelViewSet):
	queryset = Eventtype.objects.all()
	serializer_class = EventTypeSerializer

	def list(self, request, *args, **kwargs): 
		instance = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(instance)
		if page is not None:
			serializer = self.get_pagination_serializer(page)
		else:
			serializer = self.get_serializer(instance, many=True)

		serializer_data = serializer.data # get the default serialized data 
		custom_data = {x['id']:{
		'name' : x['name'], 
		'formsignupid' : x['formsignupid'],
		'formfeedbackid' : x['formfeedbackid'],
		'formproposalid' : x['formproposalid']} for x in serializer_data} # create your custom response data
		return Response(custom_data) # create response with this custom data 

class AnswerStatusView(viewsets.ModelViewSet):
	queryset = AnswerStatus.objects.all()
	serializer_class = AnswerStatusSerializer

	def list(self, request, *args, **kwargs): 
		instance = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(instance)
		if page is not None:
			serializer = self.get_pagination_serializer(page)
		else:
			serializer = self.get_serializer(instance, many=True)

		serializer_data = serializer.data # get the default serialized data 
		custom_data = {x['id']:{"name": x['name'], "color": x['color']} for x in serializer_data} # create your custom response data
		return Response(custom_data) # create response with this custom data 

class FormTypeView(viewsets.ModelViewSet):
	queryset = FormType.objects.all()
	serializer_class = FormTypeSerializer

	def list(self, request, *args, **kwargs): 
		instance = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(instance)
		if page is not None:
			serializer = self.get_pagination_serializer(page)
		else:
			serializer = self.get_serializer(instance, many=True)

		serializer_data = serializer.data # get the default serialized data 
		custom_data = {x['id']:{"name": x['name'], "color": x['color']} for x in serializer_data} # create your custom response data
		return Response(custom_data) # create response with this custom data 

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class FormView(viewsets.ModelViewSet):
	queryset = Form.objects.all().prefetch_related("answers").annotate(responses=Count("answers", distinct=True))
	serializer_class = FormSerializer

	def get_serializer_class(self):
		if (self.action=='list'):
			return FormListSerializer
		if (self.action=='update' or self.action=='partial_update') and not self.get_object().editable:
			return FormEditSerializer
		return self.serializer_class

	def get_queryset(self):
		queryset = Form.objects.all() \
		.prefetch_related("answers").annotate(responses=Count("answers", distinct=True)) \
		.prefetch_related("events_signup").annotate(signup_uses=Count("events_signup", distinct=True)) \
		.prefetch_related("events_feedback").annotate(feedback_uses=Count("events_feedback", distinct=True))

		type = self.request.query_params.get('type', None)
		hidden = self.request.query_params.get('hidden', None)
		if hidden is None and self.action=='list':
			queryset = queryset.filter(hidden=False)
		if type is not None:
			queryset = queryset.filter(type=type, hidden=False)
		return queryset

class FormAnswerView(viewsets.ModelViewSet):
	queryset = FormAnswer.objects.all()
	serializer_class = FormAnswerSerializer

	def get_queryset(self):
		queryset = FormAnswer.objects.prefetch_related('answerer').prefetch_related('editor').prefetch_related('event') \
		.prefetch_related('event__certificate').prefetch_related('event__ticket')
		form = self.request.query_params.get('form', None)
		event = self.request.query_params.get('event', None)
		user = self.request.query_params.get('user', None)
		editor = self.request.query_params.get('editor', None)
		status = self.request.query_params.get('status', None)
		if status is not None:
			status = status.split(',')
			queryset = queryset.filter(status__in=status)
		if form is not None:
			queryset = queryset.filter(form=form)
		if event is not None:
			queryset = queryset.filter(event=event)
		if user is not None:
			queryset = queryset.filter(answerer=user)
		if editor is not None:
			queryset = queryset.filter(editor=editor)
		return queryset

	def perform_create(self, serializer):
		if self.request.user.is_anonymous:
			serializer.save(answerer=None)
		else:
			serializer.save(answerer=self.request.user)
		form = Form.objects.get(pk=self.request.data["form"])
		if form.editable:
			form.editable = False
			form.save()
		if form.type.id == 2:
			event = Event.objects.get(pk=self.request.data["event"])
			event.state += 1;
			event.save()

	def perform_destroy(self, instance):
		if (instance.form.answers.count() == 1):
			instance.form.editable = True
			instance.form.save()
		instance.delete()

	def perform_update(self, serializer):
		if self.request.user.is_anonymous:
			serializer.save(editor=None, status=AnswerStatus.objects.get(pk=1))
		else:
			serializer.save(editor=self.request.user, status=AnswerStatus.objects.get(pk=1))

class MyFormAnswerView(viewsets.ModelViewSet):
	queryset = FormAnswer.objects.all()
	serializer_class = FormAnswerSerializer

	def get_queryset(self):
		queryset = FormAnswer.objects.prefetch_related('answerer').prefetch_related('editor').prefetch_related('event') \
		.prefetch_related('event__certificate').prefetch_related('event__ticket')
		form = self.request.query_params.get('form', None)
		event = self.request.query_params.get('event', None)
		status = self.request.query_params.get('status', None)
		user = self.request.user
		if status is not None:
			status = status.split(',')
			queryset = queryset.filter(status__in=status)
		if form is not None:
			queryset = queryset.filter(form=form)
		if event is not None:
			queryset = queryset.filter(event=event)
		if not self.request.user.is_anonymous:
			queryset = queryset.filter(answerer=user)
		else:
			queryset = queryset.none()
		return queryset

	def perform_create(self, serializer):
		if self.request.user.is_anonymous:
			serializer.save(answerer=None)
		else:
			serializer.save(answerer=self.request.user)
		form = Form.objects.get(pk=self.request.data["form"])
		if form.editable:
			form.editable = False
			form.save()
		if form.type.id == 2:
			event = Event.objects.get(pk=self.request.data["event"])
			event.state += 1;
			event.save()

	def perform_destroy(self, instance):
		if (instance.form.answers.count() == 1):
			instance.form.editable = True
			instance.form.save()
		instance.delete()

	def perform_update(self, serializer):
		if self.request.user.is_anonymous:
			serializer.save(editor=None, status=AnswerStatus.objects.get(pk=1))
		else:
			serializer.save(editor=self.request.user, status=AnswerStatus.objects.get(pk=1))

class FormAnswerStatus(viewsets.ModelViewSet):
	queryset = FormAnswer.objects.all()
	serializer_class = FormAnswerStatusSerializer

	def perform_update(self, serializer):
		if self.request.user.is_anonymous:
			serializer.save(editor=None)
		else:
			serializer.save(editor=self.request.user)

		answer = self.get_object()
		form = answer.form
		if form.type.id == 2:
			event = answer.event
			if answer.status.id == 2:
				event.state = 2;
				event.save()

	def get_queryset(self):
		queryset = FormAnswer.objects
		form = self.request.query_params.get('form', None)
		event = self.request.query_params.get('event', None)
		user = self.request.query_params.get('user', None)
		editor = self.request.query_params.get('editor', None)
		if form is not None:
			queryset = queryset.filter(form=form)
		if event is not None:
			queryset = queryset.filter(event=event)
		if user is not None:
			queryset = queryset.filter(answerer=user)
		if editor is not None:
			queryset = queryset.filter(editor=editor)
		return queryset

	def list(self, request, *args, **kwargs): 
		instance = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(instance)
		if page is not None:
			serializer = self.get_pagination_serializer(page)
		else:
			serializer = self.get_serializer(instance, many=True)

		serializer_data = serializer.data # get the default serialized data 
		custom_data = {x['id']:x['status'] for x in serializer_data} # create your custom response data
		return Response(custom_data) # create response with this custom data 

from django.conf import settings
from django.views.generic.base import TemplateView

from pprint import pprint
from django.shortcuts import HttpResponseRedirect
class IndexTemplateView(TemplateView):
	def dispatch(self, request, *args, **kwargs):
		request_path = self.request.path.split('/')
		page = request_path[2].lower()
		user = self.request.user
		if (page == ''):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
			if not user.groups.filter(name__in=['administrator']).exists():
				return HttpResponseRedirect('/forms/noaccess')
		elif (page == 'respond'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
		elif (page == 'responses'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
			if not user.groups.filter(name__in=['proponent', 'administrator']).exists():
				return HttpResponseRedirect('/forms/noaccess')
		elif (page == 'createform'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
			if not user.groups.filter(name__in=['administrator']).exists():
				return HttpResponseRedirect('/forms/noaccess')
		elif (page == 'chooseform'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
			if not user.groups.filter(name__in=['proponent', 'administrator']).exists():
				return HttpResponseRedirect('/forms/noaccess')
		elif (page == 'checkin'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
			if not user.groups.filter(name__in=['proponent', 'administrator']).exists():
				return HttpResponseRedirect('/forms/noaccess')
		elif (page == 'validate'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
			if not user.groups.filter(name__in=['proponent', 'administrator']).exists():
				return HttpResponseRedirect('/forms/noaccess')
		elif (page == 'certificate'):
			pass
		elif (page == 'createcertificate'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
			if not user.groups.filter(name__in=['proponent', 'administrator']).exists():
				return HttpResponseRedirect('/forms/noaccess')
		elif (page == 'ticket'):
			pass
		elif (page == 'createticket'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
			if not user.groups.filter(name__in=['proponent', 'administrator']).exists():
				return HttpResponseRedirect('/forms/noaccess')
		elif (page == 'myevents'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
			if not user.groups.filter(name__in=['administrator', 'proponent']).exists():
				return HttpResponseRedirect('/forms/noaccess')
		elif (page == 'myparticipations'):
			if not user.is_authenticated:
				return HttpResponseRedirect('/users/accounts/login')
		return super(IndexTemplateView, self).dispatch(request, *args, **kwargs)

	def get_template_names(self):
		template_name = "forms.html"
		return template_name