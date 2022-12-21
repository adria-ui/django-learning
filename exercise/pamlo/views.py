from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Helo world")

def myfirstpage(request):
    return render(request,'index.html')
    
def mysecondpage(request):
    return render(request,'second.html')    