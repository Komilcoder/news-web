from django import forms
from .models import News
from django.forms import ModelForm


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['description','image','body']
        exclude = ['user']