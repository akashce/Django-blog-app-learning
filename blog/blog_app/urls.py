from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('link/',views.link,name='link'),
    path('add-blog/',views.addblog,name='add_blog'),
    path('<id>/', views.detail_view, name='detail_view' ), 
    path('<id>/update', views.update_view, name='update_view' ),
]
