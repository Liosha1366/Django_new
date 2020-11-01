from django import forms



class CreateAut_bookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True)
    # last_name = forms.CharField( max_length=50, required=True) 
    # description = forms.CharField( max_length=500, required=True)

class UpdateAut_bookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True)
    pk = forms.CharField(widget=forms.HiddenInput)

class CreatePublishForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    # address = forms.CharField( max_length=50, required=True) 
    # city = forms.CharField( max_length=500, required=True)
    # country = forms.CharField( max_length=500, required=True)

class UpdatePublishForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    pk = forms.CharField(widget=forms.HiddenInput)

class CreateSerisForm(forms.Form):
    number = forms.CharField(max_length=50, required=True)
    number_type = forms.CharField( max_length=50, required=True) 

class UpdateSerisForm(forms.Form):
    number = forms.CharField(max_length=50, required=True)
    pk = forms.CharField(widget=forms.HiddenInput)

class CreateGenreForm(forms.Form):
    gener_tab = forms.CharField(max_length=50, required=True)
    number_type = forms.CharField( max_length=50, required=True) 
    
class UpdateGenreForm(forms.Form):
    gener_tab = forms.CharField(max_length=50, required=True)
    pk = forms.CharField(widget=forms.HiddenInput)


# class CreateHallFrom(forms.ModelForm):
#     class Meta:
#         model = models.Hall
#         fields = '__all__'

    # def clean(self):
    #     return super{}.clean()
    
