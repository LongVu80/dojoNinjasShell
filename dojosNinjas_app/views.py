from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):

    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all(),
    }
    return render(request, "index.html", context)

def create_dojo(request):
    print(request.POST)
    
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )
    return redirect("/")

def delete_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id = dojo_id)
    dojo.delete()
    return redirect("/")

def create_ninja(request):
    print(request.POST['dojo_id'])
    ninjas_dojo = Dojo.objects.get(id=request.POST['dojo_id'])
    Ninja.objects.create(
        dojo = ninjas_dojo,
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name']
    )
    return redirect("/")

def count_ninjas(request, dojo_id):
    dojo = Dojo.objects.get(id = dojo_id)
    count = 0
    for ninja in dojo.ninjas:
        count +=1
    print(count)
    return redirect("/")
    
def delete_ninja(request, ninja_id):
    ninja = Ninja.objects.get(id = ninja_id)
    ninja.delete()
    return redirect("/")
