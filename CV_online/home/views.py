from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context=context)

def about(request):
    context = {}
    return render(request, 'about.html', context=context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context=context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context=context)