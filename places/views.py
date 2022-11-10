from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.template import context
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required
from .models import *

from django.views.generic.detail import DetailView

from django.shortcuts import get_object_or_404
from django.views import View


# Create your views here.
def home (request):
	return render(request,'Home.html')

def contact (request):
	return render(request,'Contact-Us.html')








#this function queries the user registration form
def Signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request, 'Register.html', {'form': form})





def park(request):

  park = park.objects.all()
  

  return render(request, 'parkdetail.html' , context)


""" def parkview(request, slug):
  if(park.objects.filter(slug=slug)):
    products = park.objects.filter(slug=slug)
    
    context= {
      'products':products, 
      
    }

    return render(request, 'parkdetail.html' , context )"""
 



