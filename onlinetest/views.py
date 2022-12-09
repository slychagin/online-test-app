from django.shortcuts import render


def home(request):
    """Render home.html file"""
    return render(request, 'home.html')
