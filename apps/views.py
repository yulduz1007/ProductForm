from django.shortcuts import render, redirect

from apps.models import Product


def product_form_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'apps/product-form.html', context=context)


def product_detail_view(request, pk):
    context = {
        'product': Product.objects.get(pk=pk)
    }
    return render(request, 'apps/productFormDetail.html', context=context)


def product_delete_view(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('product-form')


def product_update_view(request, pk):
    if request.method == "POST":
        title = request.POST.get('name')
        Product.objects.filter(pk=pk).update(name=title)
    return redirect('product-form')



