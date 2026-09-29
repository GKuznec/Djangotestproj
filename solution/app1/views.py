from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
import random
import json
from .models import USER, TRANSACTION
def first_page(request):
    if request.method == 'POST':
        print(request.POST.get('balance'))
        print(request.POST.get('expenses'))
        print(request.POST.get('incomes'))


    return render(request, "index.html")

def all_users(request):
    context = {
        "users": USER.objects.all(),
        "transactions": TRANSACTION.objects.all(),
    }

    return render(request, "allusers.html",context=context)


