from django.shortcuts import render
from django.http import HttpResponse
#def index(request):
    #return render(request, 'hello world')

def index(request):
    return HttpResponse("hello world python")