from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home (request):
	return render(request,'Home.html')

def contact (request):
	return render(request,'Contact-Us.html')

def login (request):
	if request.method == "POST":
		username = request.POST["email"]
		password = request.POST["password"]
		user = authenticate(username=username, password=password)
		if user is not None:
			redirect('/')
	return render(request,'Login.html')

def register (request):
	message=""
	if request.method == "POST":
		username = request.POST["name"]
		email = request.POST["email"]
		password = request.POST["password"]
		user = User()
		user.email = email
		user.password = password
		user.username = username
		person = user.save()
		#user = authenticate(username=username, password=password)

		return redirect("login")
		
	
	
	return render(request,'Register.html',{"message":message})
