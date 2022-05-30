from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=125)
    content = models.CharField(max_length=1024) # TextField
    date_created = models.DateField()

    def __str__(self):
        return f'Article {self.date_created} {self.title}'