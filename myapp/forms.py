from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product #создала форму на основе Product
        fields = ['name', 'price' , 'description']