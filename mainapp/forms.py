from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Get_started

class Get_startedForm(ModelForm):
	class Meta:
		model = Get_started
		fields = ["name_user", "email_user", "message"]
		
		widgets = {
			"name_user": TextInput(attrs = {
				'id': 'name-name'
			}),
			"email_user": EmailInput(attrs = {
				'id': 'email-email'
			}),
			"message": Textarea(attrs = {
				'id': 'message-message'
			})
		}