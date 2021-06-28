from django.db import models
from  Configuration.models import Common
from Brands.models import Brands
# Create your models here.

class Usertype(Common):
	user_type = models.CharField(max_length=50,unique=True)

	def __str__(self):
		return self.user_type

class Staff(Common):
	user_type = models.ForeignKey(Usertype,on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	address = models.TextField()
	company = models.ForeignKey(Brands,on_delete=models.CASCADE)