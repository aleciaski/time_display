from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'time_display/index.html', context)

# Create your views here.


# def index(request):
# 	response= "hello i am your first request!"
# 	return HttpResponse(response)

# def yourMethodFromUrls(request):
#     context = {
#         "somekey":"somevalue"
#     }
#     return render(request,'appname/page.html', context)