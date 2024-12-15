from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/<int:id>', views.products_catagory, name='products_catagory')

]