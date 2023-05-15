from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.shops.models import Product

User = get_user_model()


class Cart(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Owner'),
        related_name='cart'
    )

    @property
    def total_price(self) -> int:
        return sum([item.total_price for item in self.cart_items.all()])

    @property
    def items_count(self) -> int:
        return self.cart_items.count()

    def add_product(self, product_id: int, quantity: int) -> None:
        product = Product.objects.get(id=product_id)
        cart_item = self.cart_items.filter(product=product).first()

        if cart_item:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            self.cart_items.create(product=product, quantity=quantity, cart=self)

    def __str__(self):
        return f"{self.owner}"

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')


class CartItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='cart_items'
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=1
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name=_('Cart'),
        related_name='cart_items'
    )

    @property
    def total_price(self) -> int:
        return self.quantity * self.product.price

    # total_price.fget.short_description = _('Total price')

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = _('Cart item')
        verbose_name_plural = _('Cart items')



# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)
#
#     def __str__(self):
#         return f' Корзина {self.user}'
#
#     def sum(self):
#         return self.product.price * self.quantity
#
#     def total_sum(self):
#         carts = Cart.objects.filter(user=self.user)
#         return sum(cart.sum() for cart in carts)
#
#     def total_quantity(self):
#         carts = Cart.objects.filter(user=self.user)
#         return sum(cart.quantity() for cart in carts)
#
#     class Meta:
#         verbose_name = "Корзина"
#         verbose_name_plural = "Корзины"


# class Cart(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         verbose_name=_('Пользователь'),
#         related_name='cart'
#     )
#     products = models.ManyToManyField(
#         Product,
#         verbose_name=_('Продукты'),
#         related_name='carts'
#     )
#     created_at = models.DateTimeField(
#         _('Дата создания'),
#         auto_now_add=True
#     )
#     updated_at = models.DateTimeField(
#         _('Дата обновления'),
#         auto_now=True
#     )
#
#     def __str__(self):
#         return f"Cart for {self.user.username}"
#
#     class Meta:
#         verbose_name = _('Корзина')
#         verbose_name_plural = _('Корзины')


# class Cart_item(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)


# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return f"Item: {self.product.name}, Quantity: {self.quantity}"

