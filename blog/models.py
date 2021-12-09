from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    date = models.DateField()
    # image = models.ImageField(upload_to="blog/images/")
    
# 以下はadminページでの表示を変更するコード
    def __str__(self):
        return self.title