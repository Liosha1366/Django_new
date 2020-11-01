import random
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from hello_world.models import models
from hello_world.models import Aut_book

from hello_world.forms import CreateAut_bookForm, UpdateAut_bookForm

# from .forms import 
# def hello_world(request):
#     result = random.randint(1, 100)
#     return HttpResponse(f"Hello world!!! With random int - {result}")


def create_aut_book_view(request):
    if request.method == 'POST':
        form = CreateAut_bookForm(data=request.POST)
    
        if form.is_valid():
            aut_book = form.cleaned_data.get('author')
            Aut_book.objects.create(author=aut_book)
    
            return HttpResponseRedirect('/')
    else:
        form = CreateAut_bookForm()
    return render(
        request, 
        template_name="hello_world/create_aut_book.html",
        context={'form': form})


def update_aut_book_view(request, pk):
    if request.method == 'POST':
        form = UpdateAut_bookForm(data=request.POST)
        if form.is_valid():    
            form.save()
            return HttpResponseRedirect('/')
    else:
        aut_book = Aut_book.objects.get(pk=pk)
        form = UpdateAut_bookForm(data=aut_book)
    return render(
        request, 
        template_name="hello_world/create_aut_book.html", 
        context={'form': form})


def delete_aut_book_view(request, pk):
    if request.method == 'POST':
        aut_book = Aut_book.objects.get(pk=pk)
    return render(
        request, 
        template_name="hello_world/delete_aut_book.html", 
        context={'aut_book': aut_book})