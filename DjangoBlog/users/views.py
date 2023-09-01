from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from .forms import UpdateUserForm, SignUpForm
from .models import CustomUser


def home(request):
    """Render the home page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered response for the home page.
    """
    return render(request, 'blog/blog-home.html', {'name': request.user})


@csrf_exempt
def login_user(request):
    """Authenticate and log in a user.

    If the request method is POST, authenticate the user based on the provided
    phone and password. If successful, log in the user; otherwise, display an
    error message.

    Args:
        request: The HTTP request object.

    Returns:
        A redirection response.
    """
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('base')
    else:
        return render(request, 'users/base.html')
    return redirect('blog-home')


def signup(request):
    """Handle user registration.

    If the request method is POST, validate the signup form and create a new user.
    If successful, authenticate the user and redirect to the base page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered response for the signup page or a redirection response.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password1']
            user = authenticate(request, phone=phone, password=password)
            if user is not None:
                print(f'{user} signed up ')
                return redirect('base')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})


def update_profile(request):
    """Update the user's profile information.

    If the user is authenticated and the request method is POST, update the user's
    profile information based on the submitted form. If successful, log in the user
    and display a success message.

    Args:
        request: The HTTP request object.

    Returns:
        A redirection response or a rendered response for the update user page.
    """
    if request.user.is_authenticated:
        current_user = CustomUser.objects.get(id=request.user.id)
        form = UpdateUserForm(
            request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, 'Profile Updated Successfully')
        else:
            return render(request, 'users/updateuser.html', {'form': form, 'name': request.user})
    return redirect('updateuser')


def logout_user(request):
    """Log out the currently authenticated user.

    Args:
        request: The HTTP request object.

    Returns:
        A redirection response.
    """
    logout(request)
    return redirect('base')
