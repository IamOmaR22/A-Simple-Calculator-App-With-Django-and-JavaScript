from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'calcu_app/index.html')

def about(request):
    return render(request, 'calcu_app/about.html')

def contact(request):
    return render(request, 'calcu_app/contact.html')
