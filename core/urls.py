from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    HomeView
)


app_name = 'core'

urlpatterns = [
    # path('', item_list, name='item-list')
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product')


]
