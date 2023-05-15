from django.urls import path

from .views import HomeView, ProductView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    # path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    # path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
]




