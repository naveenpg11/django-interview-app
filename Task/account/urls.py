from django.conf.urls import url
from .import views
from django.contrib.auth.views import login, logout

urlpatterns=[
	url(r'^login/$', login ,{'template_name':'login.html'}, name="login"),
	url(r'^logout/$', logout ,{'template_name':'logout.html'}, name="logout"),
	url(r'^register/$', views.register, name='register'),

]
