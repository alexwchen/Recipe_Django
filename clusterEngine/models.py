from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200) 
    ingredient = models.TextField()
    method = models.TextField()
    
    def __unicode__(self):
        return self.title
