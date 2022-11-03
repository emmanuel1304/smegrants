from django.shortcuts import render, redirect 
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Photos
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def home(request):
    photo = Photos.objects.all()
    context = {'photo': photo}
    return render(request, 'smeapp/home.html', context)


def application(request):
    return render(request, 'smeapp/application.html')





def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'smeapp/login.html', context={"form":form})    

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return redirect('/login')
    else:
        form = NewUserForm()

    context = {"form": form}

    return render(request, 'smeapp/register.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("smeapp:login")    