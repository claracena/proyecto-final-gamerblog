from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import *
from account.models import *

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
            messages.error(request, 'Complete correctamente los datos')
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
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
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

@login_required(login_url='login')
def profileView(request):
    return render(request, 'account/profile.html', {})

@login_required(login_url='login')
def profileEdit(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            id_form = form.save(commit=False)
            id_form.save()
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('profile')

    return render(request, 'account/profile-edit.html', {})

def userProfile(request, pk):
    try:
        user = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        destination = get_redirect_if_exists(request)
        if destination:
            return redirect(destination)
        return redirect('home')

    return render(request, 'account/user-profile.html', {'data': user})