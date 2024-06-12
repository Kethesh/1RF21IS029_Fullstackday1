from django.shortcuts import render
from math import factorial

def factorial_view(request):
    number = request.GET.get('number')
    factorial_result = None
    if number:
        number = int(number)
        factorial_result = factorial(number)
    return render(request, 'app4/index.html', {'factorial': factorial_result})