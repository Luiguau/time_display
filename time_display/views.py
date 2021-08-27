# Create your views here.
from django.shortcuts import render
from time import gmtime, localtime, strftime

# Create your views here.
def index(request):
    context = {
        "time_local_date": strftime("%b %d, %Y", localtime()),
        "time_local_time": strftime("%H:%M %p", localtime()),
        "time_gm_date": strftime("%b %d, %Y", gmtime()),
        "time_gm_time": strftime("%H:%M %p", gmtime()),
    }
    return render(request,'index.html', context)