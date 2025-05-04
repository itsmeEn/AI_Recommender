import os
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
import google.generativeai as genai


def generate_tags(product_name, description):
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    prompt = f"Suggest 3 relevant tags for a product named '{product_name}' with description: '{description}'. Return as a comma-separated list."
    # Use available and supported model 'gemini-1.5-flash'
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt])
    tags_text = response.text.strip()
    tags = [tag.strip() for tag in tags_text.split(",") if tag.strip()]
    return tags

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            tags = generate_tags(form.cleaned_data['name'], form.cleaned_data['description'])
            Product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                category=form.cleaned_data['category'],
                tags=tags
            ).save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})