from django.urls import path

from .views import HomeView, ProductView, my_form_view

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    path('myform/', my_form_view, name='myform_view'),
]




