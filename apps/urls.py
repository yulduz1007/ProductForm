from django.urls import path

from apps.views import product_form_view, product_detail_view, product_update_view, product_delete_view

urlpatterns = [
    path('', product_form_view, name="product-form"),
    path('product-detail/<int:pk>', product_detail_view, name="product-detail"),
    path('product/update/<int:pk>', product_update_view, name="product-update"),
    path('product/delete/<int:pk>', product_delete_view, name="product-delete"),
]
