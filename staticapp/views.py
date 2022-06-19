from django.shortcuts import render
from random import randrange

def background():
    number = randrange(1, 10)
    return f'{number:02d}'

# Create your views here.
def home(request):
    context = {'bg': f'bg-{background()}.jpg'}
    return render(request, 'staticapp/inicio.html', context)