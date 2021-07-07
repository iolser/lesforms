from django.contrib import admin

from .models import Form, FormAnswer, AnswerStatus, FormType, Certificate, Ticket
from resources.models import Event, Eventtype

# Register your models here.

admin.site.register(Form)
admin.site.register(FormAnswer)
admin.site.register(AnswerStatus)
admin.site.register(FormType)
admin.site.register(Event)
admin.site.register(Eventtype)
admin.site.register(Certificate)
admin.site.register(Ticket)