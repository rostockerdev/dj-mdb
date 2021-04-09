from django.db import models

class POSTGRESModel(models.Model):

    title = models.CharField(max_length=32)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title