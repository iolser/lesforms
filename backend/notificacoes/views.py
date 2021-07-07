from django.http import HttpResponse
from .models import *
from resources.models import *
import math

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import *
from django.conf import settings
from django.contrib.auth.models import Group

from django.core.paginator import Paginator

from notifications.signals import notify
from django.utils import timezone

from datetime import datetime, timedelta

from .forms import *

from django.http import HttpResponseRedirect

from enum import Enum


def apagar_notificacao_automatica(request, id ,nr):
	''' Apagar uma notificação automática '''
	if request.user.is_authenticated:
		user = get_user(request)
	else:
		return redirect('utilizadores:mensagem', 5)
	try:    
		notificacao = Notificacao.objects.get(id=nr)
	except:
		return redirect("utilizadores:mensagem", 5)
	if notificacao == None:
		return redirect("utilizadores:mensagem", 5)
	notificacao.delete()

	page=request.GET.get('page')
	response = redirect('notificacoes:categorias-notificacao-automatica', id, 0)
	response['Location'] += '?page='+page
	return response


def limpar_notificacoes(request, id):
	''' Apagar notificacoes de um utilizadore por categorias '''
	if request.user.is_authenticated:
		user = get_user(request)
	else:
		return redirect('utilizadores:mensagem', 5)
	if id == 1:
		notificacoes = user.notifications.unread() 
	elif id ==2:
		notificacoes = user.notifications.read() 
	elif id == 3:
		notificacoes = Notificacao.objects.filter(recipient_id=user , public=False)
	elif id ==4:    
		notificacoes = Notificacao.objects.filter(recipient_id=user , public=True)
	elif id == 5:
		notificacoes = Notificacao.objects.filter(recipient_id=user , level="info")
	elif id ==6:  
		notificacoes = Notificacao.objects.filter(recipient_id=user , level="warning")
	elif id ==7: 
		notificacoes = Notificacao.objects.filter(recipient_id=user , level="error")
	elif id ==8:  
		notificacoes = Notificacao.objects.filter(recipient_id=user , level="success")
	else:
		notificacoes = user.notifications.all()
	for x in notificacoes:
		x.delete()

	return redirect('notificacoes:categorias-notificacao-automatica',0,0)




def marcar_como_lida(request):
	''' Marcar todas as notificações de um utilizador como lidas '''
	if request.user.is_authenticated:
		user = get_user(request)
	else:
		return redirect('utilizadores:mensagem', 5)
	user.notifications.mark_all_as_read(user)
	return redirect('notificacoes:categorias-notificacao-automatica',0,0)






def sem_notificacoes(request, id):
	''' Página quando não existem notificacoes '''
	if request.user.is_authenticated:
		user = get_user(request)
	else:
		return redirect('utilizadores:mensagem', 5)

	return render(request, 'notificacoes/sem_notificacoes.html', {
		'categoria':id,
	})




def categorias_notificacao_automatica(request, id, nr):
	''' Ver notificações automáticas por categorias '''
	if request.user.is_authenticated:
		user = get_user(request)
	else:
		return redirect('utilizadores:mensagem', 5)
	x = 0   
	if id == 1:
		notificacoes = user.notifications.unread().order_by('-id') 
	elif id ==2:
		notificacoes = user.notifications.read().order_by('-id') 
	elif id == 3:
		notificacoes = Notificacao.objects.filter(recipient_id=user , public=False).order_by('-id')
	elif id ==4:    
		notificacoes = Notificacao.objects.filter(recipient_id=user , public=True).order_by('-id')
	elif id == 5:
		notificacoes = Notificacao.objects.filter(recipient_id=user , level="info").order_by('-id')
	elif id ==6:  
		notificacoes = Notificacao.objects.filter(recipient_id=user , level="warning").order_by('-id')
	elif id ==7: 
		notificacoes = Notificacao.objects.filter(recipient_id=user , level="error").order_by('-id')
	elif id ==8:  
		notificacoes = Notificacao.objects.filter(recipient_id=user , level="success").order_by('-id')
	else:
		notificacoes = user.notifications.all().order_by('-id')
	
	x = len(notificacoes)
	if nr!=0:
		try:
			notificacao = Notificacao.objects.get(id=nr)
		except:  
			if x>0:
				notificacao = notificacoes[0]
			else:
				return redirect("notificacoes:sem-notificacoes", id)      
	else:
		if x>0:
			notificacao = notificacoes[0]
		else:
			return redirect("notificacoes:sem-notificacoes", id)    
	nr_notificacoes_por_pagina = 15
	paginator= Paginator(notificacoes,nr_notificacoes_por_pagina)
	page=request.GET.get('page')
	notificacoes = paginator.get_page(page)
	total = x
	if notificacao != None:
		notificacao.unread = False
		notificacao.save()
	else:
		return redirect("utilizadores:mensagem", 5)
	return render(request, 'notificacoes/detalhes_notificacao_automatica.html', {
		'atual': notificacao, 'notificacoes':notificacoes,'categoria':id,'total':total
	})

class NotificationAddr(Enum):
	INVALIDAR_PROPOSTA = "invalidar_proposta"
	VALIDAR_PROPOSTA = "validar_proposta"
	RECUSAR_INSCRICAO = "recusar_inscricao"
	CANCELAR_INSCRICAO = "cancelar_inscricao"
	RECUSAR_LOGISTICA_LOCATION = "recusar_logisitica_loc"
	ATRIBUIR_LOGISTICA_LOCATION = "atribuir_logistica_loc"
	RECUSAR_LOGISTICA_EQUIP = "recusar_logistica_equip"
	ATRIBUIR_LOGISTICA_EQUIP = "atribuir_logistica_equip"
	RECUSAR_LOGISTICA_SERVICE = "recusar_logistica_service"
	ATRIBUIR_LOGISTICA_SERVICE = "atribuir_logistica_service"


def enviar_notificacao_automatica(request, sigla, id, description=""):
	''' Envio de notificação automatica '''
	if request.user.is_authenticated:
		user_sender = get_user(request)
	elif sigla!="validarRegistosPendentes":
		return redirect('utilizadores:mensagem', 5)

	if sigla == NotificationAddr.CANCELAR_INSCRICAO:
		answer = FormAnswer.objects.get(id=id)
		title = "Inscrição cancelada"
		description = "Inscrição no evento " + answer.event.name + " foi cancelada com sucesso."
		recipient = answer.answerer
		notify.send(sender=get_user(request), recipient=recipient, verb=description, action_object=answer,
			target=None, level="success", description=title, public=False, timestamp=timezone.now())
	# if sigla == NotificationAddr.RECUSAR_INSCRICAO:
	# 	event = Even
	# 	title = "Inscrição cancelada"
	# 	description = "A sua inscrição foi cancelada"
	# 	user_recipient = Generaluser.objects.get(user_ptr=id)
		
	# if sigla == NotificationAddr.INVALIDAR_PROPOSTA:
	# 	desc = "Proposta invalidada"
	# 	verb = "A sua proposta foi "

	if sigla == NotificationAddr.RECUSAR_LOGISTICA_LOCATION:
		loc = Locationuse.objects.get(id=id)
		title = "Logistica localização recusada"
		description = "O seu pedido de logistica foi recusado para o evento" + loc.event.name
		recipient = User.objects.get(id=loc.event.organizer.generaluser_ptr.user_ptr.id)
		notify.send(sender=get_user(request), recipient=recipient, verb=description, action_object=loc,
			target=None, level="warning", description=title, public=False, timestamp=timezone.now())
	elif sigla == NotificationAddr.ATRIBUIR_LOGISTICA_LOCATION:
		loc = Locationuse.objects.get(id=id)
		title = "Logistica localização atribuida"
		description = "O seu pedido de logistica foi aceite para o evento" + loc.event.name
		recipient = User.objects.get(id=loc.event.organizer.generaluser_ptr.user_ptr.id)
		notify.send(sender=get_user(request), recipient=recipient, verb=description, action_object=loc,
			target=None, level="success", description=title, public=False, timestamp=timezone.now())
	if sigla == NotificationAddr.RECUSAR_LOGISTICA_EQUIP:
		item = Itemuse.objects.get(id=id)
		title = "Logistica equipamento recusada"
		description = "O seu pedido de logistica foi recusado para o evento" + item.event.name
		recipient = User.objects.get(id=item.event.organizer.generaluser_ptr.user_ptr.id)
		notify.send(sender=get_user(request), recipient=recipient, verb=description, action_object=item,
			target=None, level="warning", description=title, public=False, timestamp=timezone.now())
	elif sigla == NotificationAddr.ATRIBUIR_LOGISTICA_EQUIP:
		item = Itemuse.objects.get(id=id)
		title = "Logistica equipamento atribuida"
		description = "O seu pedido de logistica foi aceite para o evento" + item.event.name
		recipient = User.objects.get(id=item.event.organizer.generaluser_ptr.user_ptr.id)
		notify.send(sender=get_user(request), recipient=recipient, verb=description, action_object=item,
			target=None, level="success", description=title, public=False, timestamp=timezone.now())
	if sigla == NotificationAddr.RECUSAR_LOGISTICA_SERVICE:
		serv = Serviceuse.objects.get(id=id)
		title = "Logistica serviço recusada"
		description = "O seu pedido de logistica foi recusado para o evento" + serv.event.name
		recipient = User.objects.get(id=serv.event.organizer.generaluser_ptr.user_ptr.id)
		notify.send(sender=get_user(request), recipient=recipient, verb=description, action_object=serv,
			target=None, level="warning", description=title, public=False, timestamp=timezone.now())
	elif sigla == NotificationAddr.ATRIBUIR_LOGISTICA_SERVICE:
		serv = Serviceuse.objects.get(id=id)
		title = "Logistica serviço atribuida"
		description = "O seu pedido de logistica foi aceite para o evento" + serv.event.name
		recipient = User.objects.get(id=serv.event.organizer.generaluser_ptr.user_ptr.id)
		notify.send(sender=get_user(request), recipient=recipient, verb=description, action_object=serv,
			target=None, level="success", description=title, public=False, timestamp=timezone.now())



######################################################### Mensagens #####################################################


# def escolher_tipo(request):
#     ''' Escolher tipo de mensagem a enviar, poderá ser uma mensagem de grupo ou individual '''
#     if request.user.is_authenticated:
#         user = get_user(request)
#     else:
#         return redirect('utilizadores:mensagem', 5)
#     return render(request, 'notificacoes/escolher_tipo_mensagem.html')


# def concluir_envio(request):
#     ''' Página de sucesso quando a mensagem é enviada '''
#     if request.user.is_authenticated:
#         user = get_user(request)
#     else:
#         return redirect('utilizadores:mensagem', 5)
#     return render(request, 'notificacoes/concluir_envio.html')



# def criar_mensagem(request, id):
#     ''' Criar uma nova mensagem tomando em consideração o tipo de utilizador que está logado atualmente no sistema '''
#     if request.user.is_authenticated: 
#         user = get_user(request) 
#         user = Utilizador.objects.get(id=user.id)
#         if user.getProfile()=="Coordenador" or user.getProfile()=="Colaborador" or user.getProfile()=="ProfessorUniversitario" :
#             return redirect('notificacoes:criar-mensagem-uo', id) 
#         elif user.getProfile()=="Administrador":
#             return redirect('notificacoes:criar-mensagem-admin', id) 
#         elif user.getProfile()=="Participante":
#             return redirect('notificacoes:criar-mensagem-participante', id) 
#         else:
#             return redirect('utilizadores:mensagem',5 ) 
#     else:
#         return redirect('utilizadores:mensagem', 5)      





# def criar_mensagem_participante(request, id):
#     ''' Criar uma nova mensagem por um participante '''
#     msg = False
#     if request.user.is_authenticated: 
#         user = get_user(request) 
#         if user.groups.filter(name = "Participante").exists() == False:
#             return redirect('utilizadores:mensagem', 5)  
#         user = Utilizador.objects.get(id=user.id)
#     else:
#         return redirect('utilizadores:mensagem', 5)      
		
#     if request.method == "POST":
#         tipo = id
#         if tipo == 0:
#             form = MensagemFormIndividualParticipante(request.POST)
#         elif tipo == 1:
#             form = MensagemFormGrupoParticipante(request.POST)
#         else:
#             return redirect("utilizadores:mensagem",5)
#         if form.is_valid():
#             titulo = form.cleaned_data.get('titulo')
#             mensagem = form.cleaned_data.get('mensagem')
#             if tipo == 0:
#                 email = form.cleaned_data.get('email')
#                 user_recipient = Utilizador.objects.get(email=email)
#                 info = InformacaoMensagem(data=timezone.now(), pendente=False, titulo = titulo,
#                                 descricao = mensagem, emissor = user , recetor = user_recipient, tipo = "Individual" , lido = False)
#                 info.save()
#                 mensagem1 = MensagemEnviada(mensagem=info)
#                 mensagem1.mensagem.lido = False
#                 mensagem1.save()
#                 mensagem2 = MensagemRecebida(mensagem=info)
#                 mensagem2.save()
#             elif tipo == 1:
#                 tipo_utilizadores = request.POST.get('filtro_tipo')
#                 if tipo_utilizadores == "Administrador":
#                     utilizadores = Administrador.objects.all()    
#                 else:
#                     return redirect("utilizadores:mensagem",5)
				
#                 for x in utilizadores:
#                     user_recipient = Utilizador.objects.get(user_ptr_id=x.utilizador_ptr_id)
#                     info = InformacaoMensagem(data=timezone.now(), pendente=True, titulo = titulo,
#                                     descricao = mensagem, emissor = user , recetor = user_recipient, tipo = "Grupo de admistradores do dia aberto" , lido = False)
#                     info.save()
#                     if user_recipient.id != user.id:
#                         tmp = MensagemRecebida(mensagem=info)
#                         tmp.save()  
#                 mensagem1 = MensagemEnviada(mensagem=info)
#                 mensagem1.mensagem.lido = False
#                 mensagem1.save()    
#             return redirect("notificacoes:concluir-envio")
#         else:
#             msg = True
#             if tipo == 0:
#                 return render(request=request,
#                     template_name="notificacoes/enviar_notificacao.html",
#                     context={"form": form,"msg":msg,})
#             elif tipo == 1:    
#                 form_group = UtilizadorFiltroParticipante(request.POST)
#                 return render(request=request,
#                             template_name="notificacoes/enviar_para_grupo.html",
#                             context={"form": form,"form_group":form_group,"msg":msg,})
#     else:
#         tipo = id
#         if tipo == 0:
#             form = MensagemFormIndividualParticipante()
#             return render(request=request,
#                   template_name="notificacoes/enviar_notificacao.html",
#                   context={"form": form,"msg":msg,})
#         elif tipo == 1:
#             formFilter = UtilizadorFiltroParticipante()
#             form = MensagemFormGrupoParticipante()
#             return render(request=request,
#                   template_name="notificacoes/enviar_para_grupo.html",
#                   context={"form": form,"form_group":formFilter,"msg":msg,})
#         else:
#             return redirect("utilizadores:mensagem",5)




# def criar_mensagem_uo(request, id):
#     ''' Criar uma nova mensagem por um colaborador, coordenador ou docente '''
#     msg = False
#     if request.user.is_authenticated: 
#         user = get_user(request) 
#         if user.groups.filter(name = "Colaborador").exists():
#             utilizador_atual_verificacao = True
#         elif user.groups.filter(name = "Coordenador").exists():
#             utilizador_atual_verificacao = True
#         elif user.groups.filter(name = "ProfessorUniversitario").exists():     
#             utilizador_atual_verificacao = True 
#         else:     
#             return redirect('utilizadores:mensagem', 5)  
#         user = Utilizador.objects.get(id=user.id)
#     else:
#         return redirect('utilizadores:mensagem', 5)      

#     if request.method == "POST":
#         tipo = id
#         if tipo == 0:
#             form = MensagemFormIndividualUO(request.POST)
#         elif tipo == 1:
#             form = MensagemFormGrupoUO(request.POST)
#         else:
#             return redirect("utilizadores:mensagem",5)
#         if form.is_valid():
#             titulo = form.cleaned_data.get('titulo')
#             mensagem = form.cleaned_data.get('mensagem')
#             if tipo == 0:
#                 email = form.cleaned_data.get('email')
#                 user_recipient = Utilizador.objects.get(email=email)
#                 if user_recipient.emailValidoUO(user.getUser().faculdade) == False:
#                     msg_erro = "Apenas pode ser enviada mensagem a coordenadores, colaboradores ou professores universitários da mesma unidade orgânica ou a administradores"
#                     msg = True
#                     erro = True
#                     return render(request=request,
#                         template_name="notificacoes/enviar_notificacao.html",
#                         context={"form": form,"msg":msg,"msg_erro":msg_erro, "erro":erro})
#                 else:        
#                     info = InformacaoMensagem(data=timezone.now(), pendente=False, titulo = titulo,
#                                     descricao = mensagem, emissor = user , recetor = user_recipient, tipo = "Individual" , lido = False)
#                     info.save()
#                     mensagem1 = MensagemEnviada(mensagem=info)
#                     mensagem1.mensagem.lido = False
#                     mensagem1.save()
#                     mensagem2 = MensagemRecebida(mensagem=info)
#                     mensagem2.save()
#             elif tipo == 1:
#                 grupo = "Grupo"
#                 tipo_utilizadores = request.POST.get('filtro_tipo')
#                 if tipo_utilizadores == "ProfessorUniversitario":
#                     utilizadores = ProfessorUniversitario.objects.filter(faculdade=user.getUser().faculdade)
#                     grupo = "Grupo de professores universitários"
#                 elif tipo_utilizadores == "Coordenador":
#                     utilizadores = Coordenador.objects.filter(faculdade=user.getUser().faculdade)
#                     grupo = "Grupo de coordenadores"
#                 elif tipo_utilizadores == "Colaborador":
#                     utilizadores = Colaborador.objects.filter(faculdade=user.getUser().faculdade)
#                     grupo = "Grupo de colaboradores"
#                 elif tipo_utilizadores == "Administrador":
#                     utilizadores = Administrador.objects.filter() 
#                     grupo = "Grupo de administradores do dia aberto"   
#                 else:
#                     return redirect("utilizadores:mensagem",5)
				
#                 for x in utilizadores:
#                     user_recipient = Utilizador.objects.get(user_ptr_id=x.utilizador_ptr_id)
#                     info = InformacaoMensagem(data=timezone.now(), pendente=True, titulo = titulo,
#                                     descricao = mensagem, emissor = user , recetor = user_recipient, tipo = grupo , lido = False)
#                     info.save()
#                     if user_recipient.id != user.id:
#                         tmp = MensagemRecebida(mensagem=info)
#                         tmp.save()  
#                 mensagem1 = MensagemEnviada(mensagem=info)
#                 mensagem1.mensagem.lido = False
#                 mensagem1.save()    
#             return redirect("notificacoes:concluir-envio")
#         else:
#             msg = True
#             if tipo == 0:
#                 return render(request=request,
#                     template_name="notificacoes/enviar_notificacao.html",
#                     context={"form": form,"msg":msg,})
#             elif tipo == 1:    
#                 form_group = UtilizadorFiltroUO(request.POST)
#                 return render(request=request,
#                             template_name="notificacoes/enviar_para_grupo.html",
#                             context={"form": form,"form_group":form_group,"msg":msg,})
#     else:
#         tipo = id
#         if tipo == 0:
#             form = MensagemFormIndividualUO()
#             return render(request=request,
#                   template_name="notificacoes/enviar_notificacao.html",
#                   context={"form": form,"msg":msg,})
#         elif tipo == 1:
#             formFilter = UtilizadorFiltroUO()
#             form = MensagemFormGrupoUO()
#             return render(request=request,
#                   template_name="notificacoes/enviar_para_grupo.html",
#                   context={"form": form,"form_group":formFilter,"msg":msg,})
#         else:
#             return redirect("utilizadores:mensagem",5)



# def criar_mensagem_admin(request, id):
#     ''' Criar uma nova mensagem por um administrador '''
#     msg = False
#     if request.user.is_authenticated: 
#         user = get_user(request) 
#         if user.groups.filter(name = "Administrador").exists() == False:
#             return redirect('utilizadores:mensagem', 5) 
#         user = Utilizador.objects.get(id=user.id)
#     else:
#         return redirect('utilizadores:mensagem', 5)      

#     if request.method == "POST":
#         tipo = id
#         if tipo == 0:
#             form = MensagemFormIndividualAdmin(request.POST)
#         elif tipo == 1:
#             form = MensagemFormGrupoAdmin(request.POST)
#         else:
#             return redirect("utilizadores:mensagem",5)
#         if form.is_valid():
#             titulo = form.cleaned_data.get('titulo')
#             mensagem = form.cleaned_data.get('mensagem')
#             if tipo == 0:
#                 email = form.cleaned_data.get('email')
#                 user_recipient = Utilizador.objects.get(email=email)
#                 info = InformacaoMensagem(data=timezone.now(), pendente=False, titulo = titulo,
#                                 descricao = mensagem, emissor = user , recetor = user_recipient, tipo = "Individual" , lido = False)
#                 info.save()
#                 mensagem1 = MensagemEnviada(mensagem=info)
#                 mensagem1.mensagem.lido = False
#                 mensagem1.save()
#                 mensagem2 = MensagemRecebida(mensagem=info)
#                 mensagem2.save()
#             elif tipo == 1:
#                 grupo = ""
#                 tipo_utilizadores = request.POST.get('filtro_tipo')
#                 if tipo_utilizadores == "Participante":
#                     utilizadores = Participante.objects.all()
#                     grupo = "Grupo de participantes"
#                 elif tipo_utilizadores == "ProfessorUniversitario":
#                     utilizadores = ProfessorUniversitario.objects.all()
#                     grupo = "Grupo de professores universitários"
#                 elif tipo_utilizadores == "Coordenador":
#                     utilizadores = Coordenador.objects.all()
#                     grupo = "Grupo de coordenadores"
#                 elif tipo_utilizadores == "Colaborador":
#                     utilizadores = Colaborador.objects.all()
#                     grupo = "Grupo de colaboradores"
#                 elif tipo_utilizadores == "Administrador":
#                     utilizadores = Administrador.objects.all() 
#                     grupo = "Grupo de administradores do dia aberto"   
#                 else:
#                     return redirect("utilizadores:mensagem",5)
				
#                 for x in utilizadores:
#                     user_recipient = Utilizador.objects.get(user_ptr_id=x.utilizador_ptr_id)
#                     info = InformacaoMensagem(data=timezone.now(), pendente=True, titulo = titulo,
#                                     descricao = mensagem, emissor = user , recetor = user_recipient, tipo = grupo , lido = False)
#                     info.save()
#                     if user_recipient.id != user.id:
#                         tmp = MensagemRecebida(mensagem=info)
#                         tmp.save()  
#                 mensagem1 = MensagemEnviada(mensagem=info)
#                 mensagem1.mensagem.lido = False
#                 mensagem1.save()    
#             return redirect("notificacoes:concluir-envio")
#         else:
#             msg = True
#             if tipo == 0:
#                 return render(request=request,
#                     template_name="notificacoes/enviar_notificacao.html",
#                     context={"form": form,"msg":msg,})
#             elif tipo == 1:    
#                 form_group = UtilizadorFiltro(request.POST)
#                 return render(request=request,
#                             template_name="notificacoes/enviar_para_grupo.html",
#                             context={"form": form,"form_group":form_group,"msg":msg,})
#     else:
#         tipo = id
#         if tipo == 0:
#             form = MensagemFormIndividualAdmin()
#             return render(request=request,
#                   template_name="notificacoes/enviar_notificacao.html",
#                   context={"form": form,"msg":msg,})
#         elif tipo == 1:
#             formFilter = UtilizadorFiltro()
#             form = MensagemFormGrupoAdmin()
#             return render(request=request,
#                   template_name="notificacoes/enviar_para_grupo.html",
#                   context={"form": form,"form_group":formFilter,"msg":msg,})
#         else:
#             return redirect("utilizadores:mensagem",5)
	



# def apagar_mensagem(request, id ,nr):
#     ''' Apagar uma mensagem '''
#     if request.user.is_authenticated:
#         user = get_user(request)
#     else:
#         return redirect('utilizadores:mensagem', 5)
#     m=""
#     msg = False
#     form = MensagemResposta()

#     try:
#         if id != 5:
#             tmp = MensagemRecebida.objects.get(mensagem=nr)
#         else:
#             tmp = MensagemEnviada.objects.get(mensagem=nr)

#         tmp.delete()
#     except:
#         return redirect('utilizadores:mensagem', 404)   
	
#     page=request.GET.get('page')
#     response = redirect('notificacoes:detalhes-mensagem', id, 0)
#     response['Location'] += '?page='+page
#     return response





# def limpar_mensagens(request, id):
#     ''' Apagar mensagens por categorias de um dado utilizador '''
#     if request.user.is_authenticated:
#         user = get_user(request)
#     else:
#         return redirect('utilizadores:mensagem', 5)

#     if id == 5:
#         notificacoes = MensagemEnviada.objects.select_related('mensagem__emissor').filter(mensagem__emissor=user.id)
#     elif id == 1:
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id,mensagem__lido=False) 
#     elif id == 2:
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id,mensagem__lido=True) 
#     elif id == 3:
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id,mensagem__pendente=False) 
#     elif id == 4:    
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id,mensagem__pendente=True)
#     else:
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id)
	
#     for x in notificacoes:
#         x.delete()

#     return redirect('notificacoes:detalhes-mensagem',id,0)




# def mensagem_como_lida(request, id):
#     ''' Marcar todas as mensagens de um utilizador como lidas '''
#     if request.user.is_authenticated:
#         user = get_user(request)
#     else:
#         return redirect('utilizadores:mensagem', 5)
#     msgs = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id)
#     for msg in msgs:
#         msg.mensagem.lido = True
#         msg.mensagem.save()
#         msg.save()
#     return redirect('notificacoes:detalhes-mensagem',0,0)






# def sem_mensagens(request, id):
#     ''' Página quando não existem mensagens '''
#     if request.user.is_authenticated:
#         user = get_user(request)
#     else:
#         return redirect('utilizadores:mensagem', 5)

#     return render(request, 'notificacoes/sem_mensagens.html', {
#         'categoria':id,
#     })




# def detalhes_mensagens(request, id, nr):
#     ''' Ver mensagens por categorias '''
#     if request.user.is_authenticated:
#         user = get_user(request)
#     else:
#         return redirect('utilizadores:mensagem', 5)
#     m=""
#     if request.method == "POST":
#         msg = True
#         form = MensagemResposta(request.POST)
#         if form.is_valid():
#             mensagem = form.cleaned_data.get('mensagem')
#             msg_id = form.cleaned_data.get('msg_atual')
#             user_sender = Utilizador.objects.get(user_ptr_id=user.id)
#             notificacao = MensagemRecebida.objects.get(id=msg_id)
#             if "Re: " in notificacao.mensagem.titulo:
#                 t = notificacao.mensagem.titulo
#             else:
#                 t = "Re: "+notificacao.mensagem.titulo
#             info = InformacaoMensagem(data=timezone.now(), pendente=False, titulo = t ,
#                             descricao = mensagem, emissor = user_sender, recetor = notificacao.mensagem.emissor, tipo = "Individual" , lido = False)
#             info.save()
#             mensagem1 = MensagemEnviada(mensagem=info)
#             mensagem1.mensagem.lido = False
#             mensagem1.save()
#             mensagem2 = MensagemRecebida(mensagem=info)
#             mensagem2.save()
#             m = "Mensagem enviada com sucesso"
#             form = MensagemResposta()
#         else:
#             m = ""  
#     else:
#         msg = False
#         form = MensagemResposta()

#     x = 0   
#     if id == 1:
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id,mensagem__lido=False).order_by('-id') 
#     elif id == 2:
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id,mensagem__lido=True).order_by('-id') 
#     elif id == 3:
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id,mensagem__pendente=False).order_by('-id') 
#     elif id == 4:    
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id,mensagem__pendente=True).order_by('-id')
#     elif id == 5:    
#         notificacoes = MensagemEnviada.objects.select_related('mensagem__emissor').filter(mensagem__emissor=user.id).order_by('-id')
#     else:
#         notificacoes = MensagemRecebida.objects.select_related('mensagem__recetor').filter(mensagem__recetor=user.id).order_by('-id')
	
#     x = len(notificacoes)
#     if nr!=0:
#         try:
#             notificacao = MensagemRecebida.objects.get(mensagem=nr)
#         except:
#             if x>0:
#                 notificacao = notificacoes[0]
#             else:
#                 return redirect("notificacoes:sem-mensagens", id)       
#     else:
#         if x>0:
#             notificacao = notificacoes[0]
#         else:
#             return redirect("notificacoes:sem-mensagens", id) 

#     nr_notificacoes_por_pagina = 5
#     paginator= Paginator(notificacoes,nr_notificacoes_por_pagina)
#     page=request.GET.get('page')
#     notificacoes = paginator.get_page(page)
#     total = x
#     if notificacao != None:
#         if id != 5:
#             notificacao.mensagem.lido = True
#             notificacao.mensagem.save()
#             notificacao.save()
#     else:
#         return redirect("utilizadores:mensagem", 5)
#     return render(request, 'notificacoes/detalhes_mensagens.html', {
#         "form": form,'atual': notificacao, 'notificacoes':notificacoes,'categoria':id,'total':total,"msg": msg,"m":m
#     })

