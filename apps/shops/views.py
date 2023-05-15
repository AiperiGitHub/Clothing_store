from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .models import Product, Order


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shops/index.html', {'products': products})


class ProductView(View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'shops/product.html', {'product': product})


def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'shops/product.html', context)


# def cart(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#
#     context = {'items':items}
#     return render(request, 'shops/cart.html', context)
#
#
# def checkout(request):
#     context = {}
#     return render(request, 'shops/checkout.html', context)
#
#
# def cart_add(request, product_id):
#     product = Product.objects.get(id=product_id)
#     carts = Cart.objects.filter(user=request.user, product=product)
#
#     if not carts.exists():
#         Cart.objects.create(user=request.user, product=product, quantity=1)
#     else:
#         cart = carts.first()
#         cart.quantity += 1
#         cart.save()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
#
#
# def cart_remove(request, cart_id):
#     cart = Cart.objects.get(id=cart_id)
#     cart.delete()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])

#
# def add_to_cart(request, product_id):
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     product = get_object_or_404(Product, pk=product_id)
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
#
#     if not item_created:
#         cart_item.quantity += 1
#         cart_item.save()
#
#     return redirect('cart:cart_view')
#
#
# def remove_from_cart(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, pk=cart_item_id)
#     cart_item.delete()
#
#     return redirect('cart:cart_view')
#
#
# def cart_view(request):
#     cart = Cart.objects.get(user=request.user)
#     cart_items = cart.items.all()
#
#     return render(request, 'cart/cart.html', {'cart': cart, 'cart_items': cart_items})
# def cart_view():
#     return None