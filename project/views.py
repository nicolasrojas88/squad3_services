from django.http import HttpResponse
#from django.shortcuts import render, redirect

def index():
    return HttpResponse("homepage.html")