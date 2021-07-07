from django.shortcuts import render, redirect
from django.contrib import messages

from forms.models import FormAnswer
from resources.models import Event, Group, Participant
from notificacoes.views import *

# Create your views here.

def registrations(request):
	if(not Participant.objects.filter(generaluser_ptr=request.user.id).exists()):
		return redirect('/pre_events/consult_events')
	allAnswers = FormAnswer.objects.filter(answerer = request.user.id)
	answers = []
	for a in allAnswers:
		if a.form.type.id == 1:
			temp = None
			query = FormAnswer.objects.filter(event=a.event, answerer=a.answerer)
			for q in query:
				if(q.form.type.id == 3):
					temp = q
			answers.append( (a, temp) ) # not a typo, it's sending a tuple as argument.
	print(answers)
	return render(request, 'registrations.html', {'answers': answers})

def cancel_registration(request, id):
	answer = FormAnswer.objects.get(
		event=Event.objects.get(id=id),
		answerer=request.user.id
	)
	# print(answer)
	enviar_notificacao_automatica(request, NotificationAddr.CANCELAR_INSCRICAO, answer.id)
	answer.delete()
	messages.success(request, "Inscrição removida com sucesso!")
	return redirect('registrations')
