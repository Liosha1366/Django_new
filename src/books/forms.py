from django import forms
from books import models



class UpdateBookForm(forms.Form):
    aut_book = forms.CharField(max_length=100, required=True)
    pk = forms.HiddenInput()

# class CreateBookForm(forms.Form):
#     aut_book = forms.CharField(max_length=100, required=True)
#     publish = forms.CharField(max_length=50, required=True)
#     # address = forms.CharField( max_length=50, required=True) 
#     # city = forms.CharField( max_length=50, required=True)
#     country = forms.CharField( max_length=50, required=True) 
#     # author = forms.CharField( max_length=00, required=True)
#     name_book = forms.CharField(max_length=50, required=True)
#     gener = forms.CharField( max_length=50, required=True) 
#     coin = forms.CharField( max_length=50, required=True)
#     # created = forms.CharField(max_length=50, required=True)
#     # updated = forms.CharField( max_length=50, required=True) 
    

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

    # def clean(self):
    #     return super().clean()