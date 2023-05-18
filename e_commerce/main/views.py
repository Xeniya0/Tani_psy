from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Индекс</h4>")

def about(request):
    return HttpResponse("<h4>Абоут</h4>")

def picture(request):
    return HttpResponse("<img src='https://web-zoopark.ru/wp-content/uploads/2018/07/1-104.jpg'>")
