from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('',views.index),
    path('about',views.about),
    path('contact_us',views.contact_us),
    path('services',views.services),
    path('donate_details',views.donate_details),
    path('products',views.products),
    path('clothing', views.clothing),
    path('bed',views.bed),
    path('food',views.food),
    path('med',views.med),
    path('kitchen',views.kitchen),
    path('communication',views.communication),
    path('go_cart/<str:product_type>/<int:product_id>/', views.go_cart, name='go_cart'),
    path('view_cart',views.view_cart, name='view_cart'),
    path('delete/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('delete', views.delete_all, name='delete_all'),
    # path('create_payment/', views.create_payment, name='create_payment'),
    path('succes',views.succes)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)