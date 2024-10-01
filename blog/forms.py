from django import forms
from .models import Document2

class YourModelForm(forms.ModelForm):
    class Meta:
        model = Document2
        fields = ['description', 'pdf', 'category', 'stream', 'year', 'course'] 


#-------------------for contact FORM---------------------------------------------
from django import forms

class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)

 