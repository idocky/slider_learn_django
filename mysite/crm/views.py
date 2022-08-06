from django.shortcuts import render
from .models import Order
from .forms import TestForm



def obj_list(request):
    object_list = Order.objects.all()
    form = TestForm()
    return render(request, 'test.html', {'object_list': object_list, 'form': form})
