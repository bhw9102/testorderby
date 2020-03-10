from django.shortcuts import render
from obt.models import Obt


def list_view_case_1(request):
    obt_qs = Obt.objects.all().order_by('v2', 'v1', 'v3', 'v4')
    return render(request, 'obt/list.html', {'obts_type_1': obt_qs})


def list_view_case_2(request):
    type_1 = Obt.objects.all().order_by('v2')
    type_2 = type_1.order_by('v1')
    type_3 = type_2.order_by('v4')
    type_4 = type_3.order_by('v3')
    type_once = Obt.objects.all().order_by('v3', 'v4', 'v1', 'v2')
    obt_qs_types = [type_1, type_2, type_3, type_4, type_once]
    return render(request, 'obt/multiple_list.html', {'obt_qs_types': obt_qs_types})


def create_list(request):
    for v1 in range(0, 5):
        for v2 in range(0, 5):
            for v3 in range(0, 5):
                for v4 in range(0, 5):
                    obt = Obt.objects.create(v1=v1, v2=v2, v3=v3, v4=v4)
                    obt.save()
    return render(request, 'obt/list.html')

