from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('price', views.price, name='price'),
    path('blog', views.blog, name='blog'),
    path('faq', views.faq, name='faq'),
    path('review', views.review, name='review'),
    path('dogovor', views.dogovor, name='dogovor'),
    path('contacts', views.contacts, name='contacts'),
    path('index', views.index, name='home')
]
