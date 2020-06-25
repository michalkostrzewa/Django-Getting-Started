from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from things.models import Thing

def thing(request):
    return render(request,"thing/thing.html",
                {"num_things": Thing.objects.count(),
                 "things": Thing.objects.all()   })

def create(request):
    return HttpResponse("create thing")

def list(request):
     return render(request,"thing/list.html",
                { "things": Thing.objects.all()   })

def update(request, id):
    T= get_object_or_404(Thing, pk=id)
    return render(request,"thing/update.html",
                    {"T": T} )

def delete(request, id):
    T= get_object_or_404(Thing, pk=id)
    return render(request,"thing/delete.html",
                    {"T": T} )