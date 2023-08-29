from django import forms
from django.core.exceptions import ValidationError
from .models import Advertisment
"""
class AdvertismentForm(forms.form):
    title=forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg'}))
    price=forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg'}))
    auction=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),required=False)
    image=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-lg'}))
    """

class AdvertismentForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['class']='form-control form-control-lg'
        self.fields['description'].widget.attrs['class']='form-control form-control-lg'
        self.fields['price'].widget.attrs['class']='form-control form-control-lg'
        self.fields['auction'].widget.attrs['class']='form-check-input'
        self.fields['image'].widget.attrs['class']='form-control form-control-lg'

        class Meta:
            model=Advertisment
            fields=('title','description','price','auction','image')

        def clean_title(self):
            title=self.cleaned_data['title']
            if title.startswith('?'):
                raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
            return title