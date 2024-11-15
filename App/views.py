from django.shortcuts import render

from App.models import ProductCard

# Create your views here.
def index(request):
    data = ProductCard.objects.all()
    return render(request, 'index.html', {'data':data})