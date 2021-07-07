from django.conf.urls import url, include
from users.views import dashboard, register
from django.urls import path
from django.contrib import admin

urlpatterns = [
	url(r"^accounts/", include("django.contrib.auth.urls")),
	url(r"^dashboard/", dashboard, name="dashboard"),
	url(r"^register/", register, name="register"),
	# path("admin/", admin.site.urls),
]
