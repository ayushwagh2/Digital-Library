from django import forms
from .models import Document2, Category2, Stream, Year


choices = Category2.objects.all().values_list('name','name')
choices2 = Stream.objects.all().values_list('name','name')
choice3 = Year.objects.all().values_list('classof', 'classof')


choice_list = []
choice_list2 = []
choice_list3 = []

for item in choices:
    choice_list.append(item)

for item in choices2:
    choice_list2.append(item)

for item in choice3:
    choice_list2.append(item)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document2
        fields = ('description', 'pdf', 'category', 'stream', 'year', 'course'  )

        widgets = {
            
            'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),  
            'stream' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),  
            'year' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),  
            'course' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),  
        }


#-------------------for contact FORM---------------------------------------------
from django import forms

class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)

 