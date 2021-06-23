from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main_page, name='main_page'),
    path('pdf', views.down_pdf, name='pdf'),
    path('sample', views.static_main, name='sample'),
    
]