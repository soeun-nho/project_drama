from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(verbose_name="제목", max_length=128)
    content=models.TextField(verbose_name="내용",default="")
    date=models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    
    def __str__(self):
        return self.title
