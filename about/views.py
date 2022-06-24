from django.shortcuts import render
from account.models import *
from django.db.models import Q

def aboutUs(request):
    result = Account.objects.filter(Q(id=1) | Q(id=2) | Q(id=3))
    return render(request, 'about/about.html', {'result': result})
