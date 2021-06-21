from django.db import models

# Create your models here.
from django.forms import ModelForm


class Photo(models.Model):
    text = models.CharField(max_length=500, default=False)
    image = models.ImageField(upload_to='images')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class PostForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['text', 'image']
