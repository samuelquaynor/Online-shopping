from django.urls import path
from .import views

app_name = 'shop_app'

urlpatterns = [
    #Url Path for views
    path('', views.index, name="index"),

    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="update_item"),

]