from django.db import models
from Configuration.models import Common
from Menu.models import Category
from Menu.models import Subcategory
# Create your models here.

class Product(Common):
	name = models.CharField(max_length=50,unique=True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	Subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
	priority = models.PositiveIntegerField()
	image = models.ImageField(upload_to='uploads/Product')
	price = models.PositiveIntegerField()
	discount_percent = models.PositiveIntegerField()
