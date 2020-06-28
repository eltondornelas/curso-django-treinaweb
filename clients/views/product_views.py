from django.shortcuts import render, redirect
from ..forms.product_forms import ProductForm
from ..entities.product import Product
from ..services import product_service


def register_product(request):
    if request.method == 'POST':
        form_product = ProductForm(request.POST)

        if form_product.is_valid():
            name = form_product.cleaned_data['name']
            description = form_product.cleaned_data['description']
            value = form_product.cleaned_data['value']

            new_product = Product(name=name, description=description,
                                  value=value)
            product_service.register_product(new_product)
            return redirect('list_products')
    else:
        form_product = ProductForm()

    return render(request, 'products/form_product.html',
                  {'form_product': form_product})


def list_products(request):
    products = product_service.list_products()
    return render(request, 'products/list_products.html',
                  {'products': products})


def list_product_id(request, id):
    product = product_service.list_product_id(id)
    return render(request, 'products/list_product.html', {'product': product})


def edit_product(request, id):
    product = product_service.list_product_id(id)
    form_product = ProductForm(request.POST or None, instance=product)

    if form_product.is_valid():
        name = form_product.cleaned_data['name']
        description = form_product.cleaned_data['description']
        value = form_product.cleaned_data['value']

        new_product = Product(name=name, description=description,
                              value=value)

        product_service.edit_product(product, new_product)
        return redirect('list_products')

    return render(request, 'products/form_product.html',
                  {'form_product': form_product})
