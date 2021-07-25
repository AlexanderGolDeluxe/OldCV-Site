from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="main_page"),
	path('ru', views.index_ru, name="main_page_ru"),
	path('contact', views.contact, name="contact"),
	path('projects', views.projects, name="projects"),
	path('ru/contact', views.contact_ru, name="contact_ru"),
	path('ru/projects', views.projects_ru, name="projects_ru")
]