from django.contrib import admin
from .models import Advertisment

class AdvAdmin(admin.ModelAdmin):
    list_display=['id','title','description','price','auction','created_date','updated_time']
    list_filter=['id','created_id']
    

    actions=['make_auction_as_false']
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self,request,queryset):
        queryset.update(auction=False)

    fieldsets=(
        ('Общее',{
            'fields':('title','description'),
        }),
        ('Финансы',{
            'fields': ('price','auction'),
            'classes':['collapse']
        })
    )

admin.site.register(Advertisment,AdvAdmin)


# Register your models here.
