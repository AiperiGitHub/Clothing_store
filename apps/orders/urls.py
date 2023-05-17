from django.urls import include, path

urlpatterns = [
    # Другие URL-маршруты вашего проекта
    path('orders/', include('apps.orders.urls')),
]