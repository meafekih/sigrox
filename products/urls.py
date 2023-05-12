from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('details/<int:id>', views.details, name='product'),
]
