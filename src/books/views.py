from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from books.models import Book

from books.forms import CreateBookForm, UpdateBookForm

# Create your views here.

# def create_book_view(request):
#     if request.method == 'POST':
#         form = CreateBookForm(data=request.POST)
#         if form.is_valid():
            
#             return HttpResponseRedirect('/')
#     else:
#         form = CreateBookForm()
#     return render(
#         request, 
#         template_name="book/create_book.html", 
#         context={'form': form})

def create_book_view(request):
    if request.method == 'POST':
        form = CreateBookForm(data=request.POST)
        if form.is_valid():
            book = form.cleaned_data.get('name')
            Book.objects.create(name=book)
    
            return HttpResponseRedirect('/')
    else:
        form = CreateBookForm()
    return render(
        request, 
        template_name="books/create_book.html",
        context={'form': form})


def update_book_view(request, pk):
    if request.method == 'POST':
        form = CreateBookForm(data=request.POST)
        if form.is_valid():    
            book_name = form.cleaned_data.get('name')
            Book.objects.create(name=book_name)
            return HttpResponseRedirect('/')
    else:
        book = Book.objects.get(pk=pk)
        form = UpdateBookForm(data={'name': book.name, 'pk': book.pk})
    return render(
        request, 
        template_name="books/create_book.html", 
        context={'form': form})


def delete_book_view(request, pk):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        book = Book.objects.get(pk=pk)
    return render(
        request, 
        template_name="books/delete_book.html", 
        context={'book': book})