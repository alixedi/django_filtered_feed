from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=256)
    pages = models.IntegerField()

    def __unicode__(self):
        return self.name
