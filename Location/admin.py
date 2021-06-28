from django.contrib import admin
from .models import state,Currency,Country
# Register your models here.

admin.site.register(state)
admin.site.register(Currency)
admin.site.register(Country)