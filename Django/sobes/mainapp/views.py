from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import GoodItem
from .forms import CreateForm


# Create your views here.
def goods_list(request):
    goods = GoodItem.objects.all()
    content = {
        'page_title': 'главная',
        'goods': goods
    }
    return render(request, 'mainapp/goods_list.html', content)


def good_create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:goods_list'))
    else:
        form = CreateForm()
    content = {
        'page_title': 'Создание товара',
        'create_form': form,
    }
    return render(request, 'mainapp/good_create.html', content)
