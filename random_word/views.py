# Create your views here.
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random

# Create your views here.
def index(request):

	if 'attempt' not in request.session:
		request.session['attempt'] = 1
	else:
		request.session['attempt'] += 1

	request.session['random_word'] = get_random_string(length=14)
	return render(request,'rw/index.html')

def reset(request):
	del request.session['attempt']
	return redirect('/random_word')
