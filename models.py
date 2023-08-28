from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User=get_user_model()

class Advertisment(models.Model):
    title= models.CharField('заголовок',max_length=128)
    description=models.TextField('описание')
    price=models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction= models.BooleanField('торг',help_text='Отметьте , если торг уместен')
    created_id=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,verbose_name='пользователь',on_delete=models.CASCADE)
    image=models.ImageField('изображение',upload_to='adv_65/')


    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_id.date()== timezone.now().date():
            created_time=self.created_id.time().strftime('%H:%M:%S')
            return format_html(
                '<span style=" color:green; font-weight:bold;">Сегодня в {}</span>',created_time
            )
        return self.created_id.strftime('%d.%m.%Y в %H:%M:%S')
    
    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date()== timezone.now().date():
            updated_time=self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style=" color:blue; font-weight:bold;">Сегодня в {}</span>',updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')
    @admin.display(description='фото')
    def get_image_html(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80 px; max-height: 80 px;" ',url=self.get_image_html()
            )
    



    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    
    class Meta:
        db_table='advertisement'



# Create your models here.
