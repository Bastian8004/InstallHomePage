from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.main),
    path('main', views.main, name="main"),
    path('zlecenia', views.gallery),
    path('kwalifikacje',views.post_list),
    path('firma', views.firma, name='Factory'),
    path('firma/<int:pk>/edit/', views.usluga_edit),
    path('kontakt', views.kontakt),

]