import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'
urlpatterns = [
    path('', mainapp.goods_list, name='goods_list'),
    path('good/create/', mainapp.good_create, name='good_create'),
    ]
