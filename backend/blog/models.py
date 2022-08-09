from django.db import models
from django import forms

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image = models.ImageField(upload_to='blog/images/',blank=True)
    date=models.DateField()

    def __str__(self):
        return self.title


class ContactForm(forms.Form):
    from_email=forms.EmailField(label='Email',required=True)
    subject=forms.CharField(label='Тема письма',required=True)
    message=forms.CharField(label='Сообщение',widget=forms.Textarea,required=True)
