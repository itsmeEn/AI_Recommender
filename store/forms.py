from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)
    price = forms.FloatField()
    category = forms.CharField(max_length=50)

    def save(self):
        if self.is_valid():
            Product(
                name=self.cleaned_data['name'],
                description=self.cleaned_data['description'],
                price=self.cleaned_data['price'],
                category=self.cleaned_data['category']
            ).save()