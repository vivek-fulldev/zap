from django.urls import path
from .views import BrandsApi, SignIn
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('brands/', BrandsApi.as_view()),
    path('signin/', SignIn.as_view()),
]
