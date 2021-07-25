from django.db import models

class Get_started(models.Model):
	name_user = models.CharField("Name", max_length = 30)
	email_user = models.CharField("Email", max_length = 50)
	message = models.TextField("Message", null = True, blank = True)
	sending_time = models.DateTimeField("Sending Time", auto_now_add = True, db_index = True)
	
	def __str__(self):
		return self.name_user
	
	class Meta:
		verbose_name = "Заявка на сотрудничество"
		verbose_name_plural = "Заявки на сотрудничество"