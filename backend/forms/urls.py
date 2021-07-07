from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken import views as authviews
from forms.views import IndexTemplateView

api = routers.DefaultRouter()
api.register('form', views.FormView)
api.register('formAnswer', views.FormAnswerView)
api.register('myFormAnswer', views.MyFormAnswerView)
api.register('formAnswerAuthor', views.FormAnswerAuthorView)
api.register('event', views.EventView)
api.register('myEvents', views.MyEventView)
api.register('answerStatus', views.AnswerStatusView)
api.register('formType', views.FormTypeView)
api.register('formAnswerStatus', views.FormAnswerStatus)
api.register('eventType', views.EventTypeView)
api.register('certificate', views.CertificateView)
api.register('user', views.UserInfoView)
api.register('ticket', views.TicketView)
api.register('checkin', views.CheckinView)
api.register('formAnswerNoAuthAuthor', views.FormAnswerAuthorNoAuthView)

urlpatterns = [
	path('', IndexTemplateView.as_view(template_name='index.html'), name="forms"),
	path('api/auth/', include('djoser.urls.authtoken')),
	path('api/', include(api.urls)),
	path('<path:resource>/', IndexTemplateView.as_view(template_name='index.html'), name="form"),	
]
