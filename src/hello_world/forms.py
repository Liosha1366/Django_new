from django import forms



class CreateAut_bookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField( max_length=50, required=True) 
    description = forms.CharField( max_length=500, required=True)

class UpdateAut_bookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True)
    pk = forms.HiddenInput()


# class CreateHallFrom(forms.ModelForm):
#     class Meta:
#         model = models.Hall
#         fields = '__all__'

    # def clean(self):
    #     return super{}.clean()
    
