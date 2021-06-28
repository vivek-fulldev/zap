import io
import re
import random

from django.shortcuts import render
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Brands
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from Configuration.models import Business
from rest_framework.views import APIView
from Location.models import Country
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.


# @method_decorator(csrf_exempt,name='dispatch')
class BrandsApi(APIView):
	def post(self,request,*args,**kwargs):
		try:
			json_data = request.body
			stream = io.BytesIO(json_data)
			pythondata = JSONParser().parse(stream)
			company = pythondata.get('company')
			email = pythondata.get('email')
			mobile = pythondata.get('mobile')
			address = pythondata.get('address')
			country = pythondata.get('country')
			business_type = pythondata.get('business_type')
			if company:
				if Brands.objects.filter(company=company):
					return HttpResponse(JSONRenderer().render({'company':'Company Name Already Exist in Our Database !'}), content_type='application/json')
				if len(company) > 50:
					return HttpResponse(JSONRenderer().render({'company':'Company Name Cannot be greater than 50 Characters !'}), content_type='application/json')
			else:
				return HttpResponse(JSONRenderer().render({'company':'Company Field Cannot be Blank !'}), content_type='application/json')
			if email:
				x = re.search("([a-zA-Z0-9]+@|@)+[a-zA-Z0-9]+(.com|.in|.net|.co.in)", email)
				if x == None:
					return HttpResponse(JSONRenderer().render({'email':'Email Id is in inappropriate form. !'}), content_type='application/json')
				if Brands.objects.filter(email=email) or User.objects.filter(username=email):
					return HttpResponse(JSONRenderer().render({'email':'Email Id Name Already Exist in Our Database !'}), content_type='application/json')
			else:
				return HttpResponse(JSONRenderer().render({'email':'Email Field Cannot be Blank !'}), content_type='application/json')
			if mobile:
				x = re.search("[0-9]{10}",mobile)
				if x == None:
					return HttpResponse(JSONRenderer().render({'mobile':'Phone No is not valid should be of 10 Characters !'}), content_type='application/json')
				if Brands.objects.filter(mobile=mobile):
					return HttpResponse(JSONRenderer().render({'mobile':'Phone No is already in the Database !'}), content_type='application/json')
			else:
				return HttpResponse(JSONRenderer().render({'mobile':'Mobile Field Cannot be Blank !'}), content_type='application/json')
			if address==None:
				return HttpResponse(JSONRenderer().render({'address':'Address Field Cannot be Blank !'}), content_type='application/json')
			if country:
				country = Country.objects.filter(id=int(country))
				if country == None:
					return HttpResponse(JSONRenderer().render({'country':'Country Name Does not exist in Database  !'}), content_type='application/json')
			else:
				return HttpResponse(JSONRenderer().render({'country':'Country Field Cannot be Blank !'}), content_type='application/json')
			if business_type:
				business_type = Business.objects.filter(id=int(business_type))
				if business_type == None:
					return HttpResponse(JSONRenderer().render({'business_type':'Business Type Name Does not exist in Database  !'}), content_type='application/json')
			else:
				return HttpResponse(JSONRenderer().render({'business_type':'Business Type Field Cannot be Blank !'}), content_type='application/json')
			u =  User.objects.create(username=email,password="5546546",is_staff=True)
			u.save()
			auth_id =  User.objects.get(username=u)
			Brands.objects.create(company = company,email=email,mobile=mobile,address=address,country=country[0],business_type=business_type[0],auth_user=auth_id,is_superuser=True)
			res = {'msg': 'Data Created'}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data, content_type='application/json')
		except Exception as e:
			print("Errorrrrrrrrrrrrrrrrr",e)
			return HttpResponse(JSONRenderer().render({'msg':'Something Went Wrong','error':str(e)}), content_type='application/json')


class SignIn(APIView):
	def post(self, request, *args, **kwargs):
		username = request.data.get("username")
		password = request.data.get("password")
		# username = User.objects.filter(username=username)
		# print("pppppppppppp",username[0].password)
		user = authenticate(username=username,password=password)
		print(user,type(user))
		# if user is not None:
		# 	if user.is_active:
		# login(request, user)
		return Response({"msg": "Successfully Logged In"})
				# else:
				# 	return Response({"msg": "Your Account is disabled !"})
			# else:
			# 	user = User.objects.filter(username=username)
			# 	print("pppppppppppppppppp", user)
			# 	if user:
			# 		password = User.objects.filter(password=password)
			# 		if password.count() == 0:
			# 			return Response({"password": "Password doesn't match !"})

			# 	else:
			# 		return Response({"email": "Email Id is not Registered in Our Database !"})
