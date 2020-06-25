from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from things.models import Thing
from django.forms import modelform_factory

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

ThingForm = modelform_factory(Thing, exclude=[]) #class

def new(request):
    if request.method == "POST":
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ThingForm()
    return render(request,"thing/new.html",
           { "form": form})