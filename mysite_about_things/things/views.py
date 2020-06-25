from django.shortcuts import render
from django.http import HttpResponse

def thing(request):
    return render(request,"thing/thing.html")

def create(request):
    return HttpResponse("create thing")

def list(request):
    return HttpResponse("list of things")

def update(request):
    return HttpResponse("update ")

def delete(request):
    return HttpResponse("delete ")