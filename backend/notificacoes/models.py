from django.db import models
from django.utils import timezone
from notifications.base.models import AbstractNotification
from resources.models import *


class Notificacao(AbstractNotification):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    class Meta(AbstractNotification.Meta):
        abstract = False
        db_table = 'Notificacao'
        app_label = 'notificacoes'


# Coloca temporariamente notificações geradas automaticamente com conteúdo informativo, quando passam 5 dias a notificação é enviada 
# e é apagada desta tabela da base de dados
class InformacaoNotificacao(models.Model):
    id = models.AutoField( primary_key=True)
    data = models.DateTimeField(default=timezone.now, db_index=True)
    pendente = models.BooleanField(null=False)
    titulo 	= models.CharField(max_length=255)
    descricao = models.CharField( max_length=255)
    emissor = models.ForeignKey(Generaluser, models.CASCADE, related_name='envia',null=True)  
    recetor = models.ForeignKey(Generaluser, models.CASCADE, related_name='recebe',null=True,blank=True)  
    tipo = models.CharField( max_length=255)	
    lido = models.BooleanField( null=False)	
    class Meta:
        db_table = 'InformacaoNotificacao'
