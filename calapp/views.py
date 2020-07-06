# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sum(request, num1, num2):
	return HttpResponse(str(num1) + " + " + str(num2) + " = " + str(num1+num2))

def diff(request, num1, num2):
	return HttpResponse(str(num1) + " - " + str(num2) + " = " + str(num1-num2))

def pro(request, num1, num2):
	return HttpResponse(str(num1) + " * " + str(num2) + " = " + str(num1*num2))

def quo(request, num1, num2):
	return HttpResponse(str(num1) + " / " + str(num2) + " = " + str(num1/num2))

def calculate(request, num1):
	return HttpResponse("square = " + str(num1**2) + ", cube = " + str(num1**3))
