from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from books.models import models

from books.forms import  CreateBookForm

# Create your views here.

def create_book_view(request):
    if request.method == 'POST':
        form = CreateBookForm(data=request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect('/')
    else:
        form = CreateBookForm()
    return render(
        request, 
        template_name="book/create_book.html", 
        context={'form': form})