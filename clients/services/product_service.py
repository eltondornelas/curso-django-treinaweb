from ..models import Product


def register_product(product):
    Product.objects.create(name=product.name, description=product.description,
                           value=product.value)


def list_products():
    return Product.objects.all()


def list_product_id(id):
    product = Product.objects.get(id=id)
    return product


def edit_product(product, new_product):
    product.name = new_product.name
    product.description = new_product.description
    product.value = new_product.value

    product.save(force_update=True)
