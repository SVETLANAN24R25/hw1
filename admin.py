from django.contrib import admin
from .models import Advertisment

class AdvAdmin(admin.ModelAdmin):
    list_display=['id','title','description','price','auction','created_date','updated_date','get_image_html']
    list_filter=['id','created_id']
    

    actions=['make_auction_as_false','make_auction_as_true']

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self,request,queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self,request,queryset):
        queryset.update(auction=True)

    fieldsets=(
        ('Общее',{
            'fields':('title','description','image'),
        }),
        ('Финансы',{
            'fields': ('price','auction'),
            'classes':['collapse']
        })
    )

admin.site.register(Advertisment,AdvAdmin)


# Register your models here.
