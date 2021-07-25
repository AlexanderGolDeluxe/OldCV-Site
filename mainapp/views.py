from django.shortcuts import render, redirect
from .forms import Get_startedForm
from .models import Get_started

def form_contact(request, lang):
	error = ''
	if request.method == 'POST':
		form = Get_startedForm(request.POST)
		if form.is_valid():
			form.save()
			error = ("Thank you! The data was sent successfully.", "Спасибо! Данные отправлены успешно.")[lang == "rus"]
		else:
			error = ("The form was filled out incorrectly.", "Форма была заполнена неверно.")[lang == "rus"]
	return error

def index(request):
	data = {
		'title': 'CV – Alexander Holubtsov',
		'error': form_contact(request, "eng"),
		'form': Get_startedForm()		
	}
	return render(request, "mainapp/index.html", data)

def index_ru(request):
	data = {
		'title': 'Резюме – Александр Голубцов',
		'error': form_contact(request, "rus"),
		'form': Get_startedForm()		
	}
	return render(request, "mainapp/index_ru.html", data)

def contact(request):
	data = {
		'title': 'Contact form',
		'error': form_contact(request, "eng"),
		'form': Get_startedForm()		
	}
	return render(request, "mainapp/contact.html", data)

def contact_ru(request):
	data = {
		'title': 'Форма обратной связи',
		'error': form_contact(request, "rus"),
		'form': Get_startedForm()		
	}
	return render(request, "mainapp/contact_ru.html", data)

def projects(request):
	data = {
		'title': 'Projects – Alexander Holubtsov'
	}
	return render(request, "mainapp/projects.html", data)

def projects_ru(request):
	data = {
		'title': 'Проекты – Александр Голубцов'
	}
	return render(request, "mainapp/projects_ru.html", data)