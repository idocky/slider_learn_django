from django.http import HttpResponse
from django.shortcuts import render
from crm import views
from cms.models import CmsSlider
from services.models import ServiceCards, ServiceTable
from crm.forms import TestForm
from crm.models import Comment

def first_page(request):
    slider_list = CmsSlider.objects.all()
    c1 = ServiceCards.objects.get(pk=1)
    c2 = ServiceCards.objects.get(pk=2)
    c3 = ServiceCards.objects.get(pk=3)
    service_list = ServiceTable.objects.all()
    form = TestForm()
    list_comment = Comment.objects.filter(com_text__contains = 'top')

    object_list = {
        'slider_list': slider_list,
        'c1': c1,
        'c2': c2,
        'c3': c3,
        'service_list': service_list,
        'form': form,
        'list_comment': list_comment,
    }
    return render(request, './index.html', object_list)

def thx_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    views.Order.objects.create(order_name= name, order_phone= phone)
    return render(request, './thanks.html')