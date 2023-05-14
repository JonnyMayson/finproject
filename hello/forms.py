from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BlogModel
from django import forms
from .models import  Category

choices = Category.objects.all().values_list('name' , 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ('title', 'title_tag', 'image', 'content','category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs = {'class': 'form-control'}),
        }



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), )
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)







