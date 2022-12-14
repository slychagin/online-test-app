from django.shortcuts import render


def register(request):
    """Render registration page"""
    return render(request, 'accounts/register.html')


def login(request):
    """Render login page"""
    return render(request, 'accounts/login.html')


def logout(request):
    """Render logout page"""
    return render(request, 'accounts/logout.html')
