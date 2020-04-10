from django.db import models
from datetime import datetime

class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    Published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.Title
