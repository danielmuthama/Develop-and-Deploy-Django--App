from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home (request):
	return render(request,'index.html')

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


