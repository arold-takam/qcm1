from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def correction(request):
    return render(request, 'correction.html')

def inscription(request):
    return render(request, 'inscription.html')