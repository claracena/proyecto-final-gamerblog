from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    data = {
        'form': ContactForm(),
    }

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
        else:
            data['form'] = form
    return render(request, 'contact/contact.html', data)

def success(request):
    return render(request, 'contact/success.html')
