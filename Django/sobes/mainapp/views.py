from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

from .models import GoodItem
from .forms import CreateForm


# Create your views here.
def goods_list(request):
    goods = GoodItem.objects.all()
    form = CreateForm()
    content = {
        'page_title': 'главная',
        'goods': goods,
        'create_form': form,
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


# def save_good_form(request, form, template_name):
#     data = dict()
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             goods = GoodItem.objects.all()
#             data['html_good_list'] = render_to_string('mainapp/goods_list.html', {
#                 'goods': goods
#             })
#     else:
#         data['form_is_valid'] = False
#         context = {'form': form}
#         data['html_form'] = render_to_string(template_name, context, request=request)
#     return JsonResponse(data)
