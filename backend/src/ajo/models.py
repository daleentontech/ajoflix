from django.db import models
from django.urls import reverse

# Create your models here.

class AjoAccount(models.Model):
	account_name = models.CharField(max_length=200)
	account_number = models.CharField(max_length=8, unique=True)
	balance = models.IntegerField()

	def __str__(self):
		return self.account_name


	def get_absolute_url(self):
		return reverse("accounts:detail", kwargs={"account_number":self.account_number})