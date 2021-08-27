# Create your views here.
from django.shortcuts import render
from time import gmtime, localtime, strftime

# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request,'index.html', context)