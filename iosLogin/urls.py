from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$',views.home, name = "homepage"),
	url(r'^login/$', views.loginController, name = "ioslogin")
	
]