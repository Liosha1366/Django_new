import random
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from hello_world.models import models
from hello_world.models import Aut_book

from hello_world.forms import CreateAut_bookForm, UpdateAut_bookForm, CreatePublishForm, UpdatePublishForm
from hello_world.forms import CreateSerisForm, UpdateSerisForm, CreateGenreForm, UpdateGenreForm

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
        form = CreateAut_bookForm(data=request.POST)
        if form.is_valid():    
            aut_book_name = form.cleaned_data.get('author')
            Aut_book.objects.create(author=aut_book_name)
            return HttpResponseRedirect('/')
    else:
        aut_book = Aut_book.objects.get(pk=pk)
        print(aut_book)
        form = UpdateAut_bookForm(data={'author': aut_book.author, 'pk': aut_book.pk})
    return render(
        request, 
        template_name="hello_world/create_aut_book.html", 
        context={'form': form})


def delete_aut_book_view(request, pk):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        aut_book = Aut_book.objects.get(pk=pk)
    return render(
        request, 
        template_name="hello_world/delete_aut_book.html", 
        context={'aut_book': aut_book})


        #=================================================================

def create_publish_view(request):
    if request.method == 'POST':
        form = CreatePublishForm(data=request.POST)
        if form.is_valid():
            publish = form.cleaned_data.get('name')
            Publish.objects.create(name=publish)
    
            return HttpResponseRedirect('/')
    else:
        form = CreatePublishForm()
    return render(
        request, 
        template_name="hello_world/create_aut_book.html",
        context={'form': form})


def update_publish_view(request, pk):
    if request.method == 'POST':
        form = CreatePublishForm(data=request.POST)
        if form.is_valid():    
            publish_name = form.cleaned_data.get('name')
            Publish.objects.create(name=publish_name)
            return HttpResponseRedirect('/')
    else:
        publish = Publish.objects.get(pk=pk)
        form = UpdatePublishForm(data={'name': publish.name, 'pk': publish.pk})
    return render(
        request, 
        template_name="hello_world/create_aut_book.html", 
        context={'form': form})


def delete_publish_view(request, pk):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        publish = Publish.objects.get(pk=pk)
    return render(
        request, 
        template_name="hello_world/delete_aut_book.html", 
        context={'publish': publish})
#======================================================================

def create_seris_view(request):
    if request.method == 'POST':
        form = CreateSerisForm(data=request.POST)
        if form.is_valid():
            seris = form.cleaned_data.get('number')
            Seris.objects.create(number=seris)
    
            return HttpResponseRedirect('/')
    else:
        form = CreateSerisForm()
    return render(
        request, 
        template_name="hello_world/create_aut_book.html",
        context={'form': form})


def update_seris_view(request, pk):
    if request.method == 'POST':
        form = CreateSerisForm(data=request.POST)
        if form.is_valid():    
            seris_name = form.cleaned_data.get('number')
            Seris.objects.create(number=seris_name)
            return HttpResponseRedirect('/')
    else:
        publish = Seris.objects.get(pk=pk)
        form = UpdateSerisForm(data={'number': seris.number, 'pk': seris.pk})
    return render(
        request, 
        template_name="hello_world/create_aut_book.html", 
        context={'form': form})


def delete_seris_view(request, pk):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        seris = Seris.objects.get(pk=pk)
    return render(
        request, 
        template_name="hello_world/delete_aut_book.html", 
        context={'seris': seris})
#=========================================================================

def create_genre_view(request):
    if request.method == 'POST':
        form = CreateGenreForm(data=request.POST)
        if form.is_valid():
            gener = form.cleaned_data.get('gener_tab')
            Seris.objects.create(gener_tab=gener)
    
            return HttpResponseRedirect('/')
    else:
        form = CreateGenreForm()
    return render(
        request, 
        template_name="hello_world/create_aut_book.html",
        context={'form': form})

def update_gener_view(request, pk):
    if request.method == 'POST':
        form = CreateGenreForm(data=request.POST)
        if form.is_valid():    
            gener_name = form.cleaned_data.get('gener_tab')
            Genre.objects.create(gener_tab=gener_name)
            return HttpResponseRedirect('/')
    else:
        gener = Genre.objects.get(pk=pk)
        form = UpdateGenreForm(data={'gener_tab': gener.gener_tab, 'pk': gener.pk})
    return render(
        request, 
        template_name="hello_world/create_aut_book.html", 
        context={'form': form})


def delete_genre_view(request, pk):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        genre = Genre.objects.get(pk=pk)
    return render(
        request, 
        template_name="hello_world/delete_aut_book.html", 
        context={'genre': genre})