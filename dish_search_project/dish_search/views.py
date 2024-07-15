# from django.shortcuts import render
#
# # Create your views here.
# def Home(request):
#     return render(request,"Home.html")
# # dish_search/views.py

from django.shortcuts import render
from django.db.models import Q
from . models import Restaurant

def Home(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Restaurant.objects.filter(Q(name__icontains=query) | Q(items__icontains=query))
    return render(request, 'Home.html', {'query': query, 'results': results})
