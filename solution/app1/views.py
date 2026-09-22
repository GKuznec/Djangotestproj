from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
import random
import json
def first_page(request):
    print(request.body)
    print(request.method)
    print(request)
    print(request.GET.dict())
    # data = json.loads(request.body)
    # name = data.get('balance')
    # print(name)
    context = {
       "expenses": random.randint(1,100),
       "incomes": 1000
    }

    return render(request, "index.html",context = context)
