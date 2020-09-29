from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import ProductModel

# Create your views here.


def baseview(request):
    return render(request, 'base.html')

def CreateView(request):
    if request.method=='POST':
        fm=ProductForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=ProductForm()
    return render(request, 'create.html', {'form': fm})


def ShowView(request):
    product=ProductModel.objects.all()
    return render(request, 'show.html', {'pro': product})


def UpdateView(request,id):
    if request.method=='POST':
        pi=ProductModel.objects.get(pk=id)
        fm=ProductForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/show')
    else:
        pi=ProductModel.objects.get(pk=id)
        fm=ProductForm(instance=pi)
    return render(request, 'update.html', {'form': fm})


def DeleteView(request,id):
    if request.method=="POST":
        pi=ProductModel.objects.get(pk=id)
        pi.delete()
        return redirect('/create')