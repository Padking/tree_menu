from django.urls import re_path
from . import views


urlpatterns = [
	re_path(r'^(.)*$', views.get_menu, name='get_menu'),
]