from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm

def registerView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('home')
        else:
            context['registration_form'] = form

    return render(request, 'account/register.html', context)

def logoutView(request):
    logout(request)
    return redirect('home')

def loginView(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    # print(request.POST['email'])
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        # print(request.POST['email'])
        # form = AccountAuthenticationForm(request.POST)
        # if form.is_valid():
        #     # print(form)
        #     email = request.POST['email']
        #     password = request.POST['password']
        #     user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('home')
        else:
            return render(request, 'account/login.html', context)

    return render(request, 'account/login.html', context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))

    return redirect

def blogView(request):
    return render(request, 'account/blog.html', {})

def profileView(request):
    return render(request, 'account/profile.html', {})