from django.urls import path

from . import views
from .views import remove_from_cart

urlpatterns = [
    path('', views.index, name='index'),
    path('product-detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product-list/', views.ProductList.as_view(), name='product_list'),
    path('product-add-cart/<int:product_pk>/', views.add_to_cart, name='add_to_cart'),
    path('product-order/', views.OrderItemsListView.as_view(), name='product_order'),
    path('about/', views.about_us, name='about_us'),
    path('personal-area/', views.personal_area, name='personal_area'),
    path('remove-from-cart/<int:order_item_pk>/', remove_from_cart, name='remove_from_cart'),
]