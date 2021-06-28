from django.db import models

# Create your models here.

class Common(models.Model):
	active_status = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True

class Business(Common):
	business_type = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Business"

	def __str__(self):
		return self.business_type