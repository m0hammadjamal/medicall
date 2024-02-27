from django.shortcuts import render
from web.models import Impression,Product

def index(request):
    impressions = Impression.objects.all()
    Products = Product.objects.all()
    context = {
        "impressions" : impressions,
        "products" : Products,
    }
    return render(request, 'index.html', context=context)