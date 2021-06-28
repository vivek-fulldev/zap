from django.db import models
from Configuration.models import Common
# Create your models here.


class state(Common):
	state = models.CharField(max_length=50,unique=True)

class Currency(Common):
	currency = models.CharField(max_length=50,unique=True)
	symbol = models.CharField(max_length=2)

	class Meta:
		verbose_name_plural = "Currencies"

	def __str__(self):
		return self.currency

class Country(Common):
	country = models.CharField(max_length=50,unique=True)
	currency = models.OneToOneField(Currency,on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Countries"
	def __str__(self):
		return self.country