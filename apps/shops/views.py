from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .models import Product


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
    context = {'products': products}
    return render(request, 'shops/index.html', context)


def my_form_view(request):
    if request.method == 'POST':
        quentity = request.POST.get('quentity')
        color = request.POST.get('color')

        # Обработка полученных данных
        # ...
        # Пример выборки цветов
        colors = ['grey', 'dark-grey', 'black']
        selected_color = colors[int(color)]

        # Передача данных в шаблон
        context = {
            'quentity': quentity,
            'selected_color': selected_color
        }

        return render(request, 'shops/index.html', context)  # Отображение результата на странице result.html

    return render(request, 'shops/index.html')

