from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Advertisment
from .forms import AdvertismentForm

def index(request):
    advert=Advertisment.objects.all()
    context={'advertisements':advert}
    return render(request,'index.html',context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def adv_post(request):
    if request.method=='POST':
        form=AdvertismentForm(request.POST,request.FILES)
        if form.is_valid():
            new_adv=form.save(commit=False)
            new_adv.user=request.user
            new_adv.save()
            url=reverse('main-page')
            return redirect(url)
    else:
        form=AdvertismentForm()

    context={'form':form}
    return render(request,'advertisment-post.html',context)
def reg(request):
    return render(request,'register.html')
    
def log(request):
    return render(request,'login.html')

def pro(request):
    return render(request,'profile.html')


    







# Create your views here.
