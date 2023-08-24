from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import updateUserForm, signUpForm
from .models import CustomUser


# Create your views here.


def home(request):
    return render(request, 'users/home.html', {'name': request.user})


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'users/home.html', {'name': user})
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('base')

    return render(request, 'users/base.html')

def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password1']
            user = authenticate(request, phone=phone, password=password)
            if user is not None:
                # login(request, user)
                print(f'{user} signed up ')
                return redirect('base')
    else:
        form = signUpForm()

    return render(request, 'users/signup.html', {'form': form})

def update_profile(request):
    if request.user.is_authenticated:
        print(request.user)
        current_user = CustomUser.objects.get(id=request.user.id)
        form = updateUserForm(
            request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, 'Profile Updated Successfully')
        else:
            return render(request, 'users/updateuser.html', {'form': form, 'name': request.user})
    return redirect('updateuser')

def logout_user(request):
    logout(request)
    return redirect('base')
