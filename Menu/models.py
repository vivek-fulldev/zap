from django.db import models
from  Configuration.models import Common

# Create your models here.

class Category(Common):
	category = models.CharField(max_length=50,unique=True)
	code = models.PositiveIntegerField()
	image = models.ImageField(upload_to='uploads/Menu')
	priority = models.PositiveIntegerField()

	def __str__(self):
		return self.category

class Subcategory(Common):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	name = models.CharField(max_length=50,unique=True)
	priority = models.PositiveIntegerField()

	def __str__(self):
		return self.name
