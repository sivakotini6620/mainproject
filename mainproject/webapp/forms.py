from django import forms
from .models import ProductModel


class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields="__all__"
        widgets = {
            'Productname': forms.TextInput(attrs={'class': 'form-control'}),
            'Productcom': forms.TextInput(attrs={'class': 'form-control'}),
            'Productid' : forms.NumberInput(attrs={'class': 'form-control'}),
            'Productmufc': forms.TextInput(attrs={'class': 'form-control'}),
            'Productcost': forms.NumberInput(attrs={'class': 'form-control'}),

        }