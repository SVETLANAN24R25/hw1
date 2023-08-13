from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')

def adv_post(request):
    return render(request,'advertisment-post.html')
def reg(request):
    return render(request,'register.html')
    
def log(request):
    return render(request,'login.html')

def pro(request):
    return render(request,'profile.html')






# Create your views here.
