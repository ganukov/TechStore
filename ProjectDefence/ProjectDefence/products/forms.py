from ProjectDefence.products.models import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {

            'name': forms.TextInput(
                attrs={'placeholder': 'Enter the Brand of the product'}
            ),
            'make': forms.TextInput(
                attrs={'placeholder': 'Enter the Model of the product'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Enter the Price of the product'}
            ),
            'image': forms.URLInput(
                attrs={'placeholder': 'Enter a correct URL for the product`s image'}
            ),
            'cpu': forms.TextInput(
                attrs={'placeholder': 'Enter the CPU stats'}
            ),
            'gpu': forms.TextInput(
                attrs={'placeholder': 'Enter the GPU stats'}
            ),
            'weight': forms.NumberInput(
                attrs={'placeholder': 'Enter the weight of the product'}
            ),
            'os': forms.TextInput(
                attrs={'placeholder': 'Enter the OS of the product'}
            ),
            'description': forms.TextInput(
                attrs={'placeholder': 'Enter a description for the product'}
            ),
        }