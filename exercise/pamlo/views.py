from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Helo world")

def myfirstpage(request):
    return render(request,'index.html')
    
def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    var ="hello world"
    brief = "Am adrian malcolm"
    fruits =["pinaplle","mango","Strawberry"]
    num1, num2 = 3 , 5 
    ans = num1 > num2
    mydictionary = {
        "var" : var,
        "msg" : brief,
        "myfruits" : fruits,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans
    }
    return render(request,'third.html',context=mydictionary)