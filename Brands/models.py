from django.db import models
from django.contrib.auth.models import User
from Location.models import Country,Currency
from Configuration.models import Business,Common
# Create your models here.

class Brands(Common):
	company = models.CharField(max_length=50,unique=True)
	email = models.EmailField(unique=True)
	mobile = models.CharField(max_length=100,unique=True)
	address = models.TextField()
	auth_user = models.OneToOneField(User,on_delete=models.CASCADE)
	country = models.ForeignKey(Country,on_delete=models.CASCADE)
	business_type = models.ForeignKey(Business,on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Brand"
		verbose_name_plural = "Brands"

	def __str__(self):
		return self.company