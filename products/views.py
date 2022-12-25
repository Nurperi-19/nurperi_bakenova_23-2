from django.shortcuts import render, redirect
from products.models import Product, Category, Review
from products.forms import ProductCreateForm, ReviewCreateForm

# Create your views here.

def main_view(request):
    return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id', 0))

        if category_id:
            products = Product.objects.filter(categories__in=[category_id])
        else:
            products = Product.objects.all()

        return render(request, 'products/products.html', context={
            'products': products
        })

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'categories': product.categories.all(),
            'review_form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                product_id=id,
                text=form.cleaned_data.get('text')
            )
            return redirect(f'/products/{id}')
        else:
            return render(request, 'products/detail.html', context={
                'product': product,
                'reviews': product.review_set.all(),
                'categories': product.categories.all(),
                'review_form': form
            })

def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context = {
            'categories': categories
        }

        return render(request, 'categories/index.html', context=context)

def product_create_view(request):
    if request.method == "GET":
        return render(request, 'products/create.html', context={
            'form': ProductCreateForm
        })

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                category=form.cleaned_data.get('category'),
                name=form.cleaned_data.get('name'),
                color= form.cleaned_data.get('color'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price', 0)
            )
            return redirect('/products/')
        else:
            return render(request, 'products/create.html', context={
                'form': form
            })

