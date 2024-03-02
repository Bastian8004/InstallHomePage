from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('oferty', views.ofert_list, name='ofert_list'),
    path('oferty/<int:pk>/', views.ofert_detail, name='ofert_detail'),
    path('zlecenia', views.gallery),
    path('kwalifikacje',views.post_list),
    path('firma', views.firma, name='Factory'),
    path('firma/<int:pk>/edit/', views.usluga_edit),
    path('kontakt', views.kontakt),


]