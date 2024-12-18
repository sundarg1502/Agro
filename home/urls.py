from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/<int:id>', views.products_catagory, name='products_catagory'),
    path('products/<str:name>', views.products_seller, name='products_seller'),
    path('register/', views.register, name='register'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("uploads/", views.uploads, name='uploads'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("user/", views.user, name='user'),
    path("user_update/", views.user_update, name='user_update'),

]