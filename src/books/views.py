from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from books.models import Book

from books.forms import CreateBookForm, UpdateBookForm

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
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

def show_book_by_pk_view(request, book_id):

    book_obj = Book.objects.get(pk=book_id)
    # con = {'book': book_obj}
    return render(
        request, 
        template_name="books/book.html",
        context={'book': book_obj},
    )


class ShowBookListView(ListView):
    template_name = "books/book_list.html"
    model = Book
    # queryset = Book.objects.all()

    def get_queryset(self):
        return super().get_queryset()[0:10]
    
class StaticView(TemplateView):
    template_name='books/static.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pop"] = 'pops'
        return context
    
#==============================================================

def create_book_view(request):
    if request.method == 'POST':
        form = CreateBookForm(data=request.POST)
        if form.is_valid():
            book = form.cleaned_data.get('aut_book')
            Book.objects.create(aut_book=book)
    
            return HttpResponseRedirect('/')
    else:
        form = CreateBookForm()
    return render(
        request, 
        template_name="books/create_book.html",
        context={'form': form})

class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['aut_book', 'publish', 'country', 'name_book', 'gener', 'coin']
    success_url="/"
    login_url = '/admin/login'
    template_name = "books/create_book.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(self.request.user, 'liosha')
    #     return context
    

def update_book_view(request, pk):
    if request.method == 'POST':
        form = CreateBookForm(data=request.POST)
        if form.is_valid():    
            book_name = form.cleaned_data.get('aut_book')
            Book.objects.create(aut_book=book_name)
            return HttpResponseRedirect('/')
    else:
        book = Book.objects.get(pk=pk)
        form = UpdateBookForm(data={'aut_book': book.aut_book, 'pk': book.pk})
    return render(
        request, 
        template_name="books/create_book.html", 
        context={'form': form})

class UpdateBookView(UpdateView):
    model = Book
    fields = ['aut_book', 'publish', 'country', 'name_book', 'gener', 'coin']
    success_url="/"
    template_name = "books/create_book.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rate"] = 2.67
        return context
    

def delete_book_view(request, pk):
    if request.method == 'POST':
        book = Book.objects.delete(pk=pk)
        return HttpResponseRedirect('/')
    else:
        book = Book.objects.get(pk=pk)
    return render(
        request, 
        template_name="books/delete_book.html", 
        context={'book': book})

class DeleteBookView(DeleteView):
    model = Book
    fields = ['aut_book', 'publish', 'country', 'name_book', 'gener', 'coin']
    success_url="/"
    template_name = "books/delete_book.html"

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect('/')
    
    
    
