from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Squirrels
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .forms import Form
import json

def Totalsquirrels(request):
    squirrels = Squirrels.objects.all()
    context = {
            'squirrels': squirrels
            }
    return render(request,'sightings1/total.html',context)
def squirrelfeatures(request,Unique_squirrel_id):
    squirrel = Squirrels.objects.get(Unique_squirrel_id=id)
    return HttpResponse(f"This is {squirrel.Unique_squirrel_id}")

def squirrelupdate(request,squirrel_id):
    Object = get_object_or_404(Squirrels,Unique_squirrel_id=squirrel_id)
    form = Form(request.POST or None,instance=Object)
    context = {'form':form}
    if form.is_valid():
        Object=form.save(commit=False)
        Object.save()
        return redirect('/sightings1/')
    else:
        context={
                'form':form,
        }
        return render(request,'sightings1/formupdate.html',context)

#class add(CreateView):
#    model = Squirrels
#    fields = '__all__'
def squirreladd(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sightings1/')
    else:
        form = Form()
        context = {'form':form,}
        return render(request,'sightings1/squirrelform.html',context)

def squirreldelete(request,squirrel_id):
    Object = get_object_or_404(Squirrels,Unique_squirrel_id=squirrel_id)
    try:
        Object.delete()
        return redirect(f'/sightings1/')
    except:
        return render(request,'sightings1/deleted.html')

import random
def showmap(request):
    sightings = Squirrels.objects.all()
    context = {
            'sightings':sightings
            }
    return render(request,'sightings1/map.html',context)

def statistics(request):
    sightings_sum = Squirrels.objects.all().count()
    juvenile_sum= Squirrels.objects.filter(Age='Juvenile').count()
    gray_sum= Squirrels.objects.filter(Primary_Fur_Color='Gray').count()
    ground_plane_location=Squirrels.objects.filter(Location='Ground Plane').count()
    running_sum = Squirrels.objects.filter(Running='TRUE').count()
    context = {
            'SIGHTING_SUM':sightings_sum,
            'JUVENILE_SUM':juvenile_sum,
            'GRAY_FUR':gray_sum,
            'GROUND_PLANE_LOCATION':ground_plane_location,
            'RUNNING':running_sum,
            }
    return render(request, 'sightings1/statistics.html',context)

# Create your views here.
