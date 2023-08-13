from django.urls import path
from .views import index,top_sellers,adv_post,reg,log,pro

urlpatterns=[
    path( '', index, name='main-page'),
    path('top-sellers/',top_sellers,name='top-sellers'),
    path('adv-post/',adv_post,name='adv-post'),
    path('reg/',reg, name='reg'),
    path('log/',log,name='log'),
    path('pro/',pro,name='pro'),
]