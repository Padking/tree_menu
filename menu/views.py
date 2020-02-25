from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_menu(request, *arg):
	return render(request, 'menu/main.html')

def index(request):
	"""Обработчик домена"""
	return HttpResponse("<h2> Главная </h2>")