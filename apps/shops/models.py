from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        _('Название'),
        max_length=255
    )
    parent = TreeForeignKey(
        'self',
        verbose_name=_('Родительская категория'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    description = models.TextField(
        _('Описание'),
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=255,
        null=True
    )
    description = models.TextField(
        _('Описание'),
        null=True,
        blank=True
    )
    price = models.PositiveIntegerField(
        _('Цена'),
        default=0
    )
    quantity = models.PositiveIntegerField(
        _('Количество в наличий'),
        default=0
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_('Категория'),
        related_name='products'
    )
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class ProductImage(models.Model):
    image = models.ImageField(
        _('Изображение'),
        null=True,
        blank=True,
        upload_to='product_images/'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Продукт'),
        related_name='images'
    )

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')


class Specification(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=255
    )
    value = models.CharField(
        _('Значение'),
        max_length=255
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Продукт'),
        related_name='specifications'
    )

    class Meta:
        verbose_name = _('Спецификация')
        verbose_name_plural = _('Спецификации')


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.address)














