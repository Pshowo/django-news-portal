from django.db import models


class News(models.Model):
    title = models.CharField(max_length=140)
    publish = models.DateTimeField(auto_now_add=True)
    body = models.TextField()



