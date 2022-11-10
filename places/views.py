from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def allplaces (request):
	return render(request,'Activities.html')