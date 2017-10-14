from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
        request.session['randString'] = get_random_string(length=14)
    context = {
            'attempt':    request.session['attempt'],
            'randString': request.session['randString']
    }
    return render(request, 'randword_app/index.html', context)

def generate(request):
    request.session['randString'] = get_random_string(length=14)
    request.session['attempt'] += 1
    return redirect(index)

def reset(request):
    request.session['attempt'] = 1
    request.session['randString'] = get_random_string(length=14)
    return redirect(index)
