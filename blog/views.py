from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'blog/home.html')

def registro(request):
    return render(request, 'blog/register.html')