from django.shortcuts import render
from django.http import HttpResponse
def offers(request):
    context = {'name': 'John'}
    return render(request, "offer\offer.html", context)


# Create your views here.
