# Create your views here.
from django.shortcuts import render
from time import gmtime, localtime, strftime
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        "time_local_date": strftime("%b %d, %Y", localtime()),
        "time_local_time": strftime("%H:%M %S", localtime()),
        "time_gm_date": strftime("%b %d, %Y", gmtime()),
        "time_gm_time": strftime("%H:%M %S", gmtime()),
		"datetime_local_date":datetime.now().strftime("%b %d, %Y"),
		"datetime_local_time":datetime.now().strftime("%H %M, %S"),
		"datetime_gm_date":datetime.now().strftime("%b %d, %Y"),
		"datetime_gm_time":datetime.now().strftime("%H %M, %S"),
    }
    return render(request,'index.html', context)