from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30,verbose_name="Başlık")
    completed = models.BooleanField(verbose_name= "Durum")
