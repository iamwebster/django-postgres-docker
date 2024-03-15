from django.db import models


class TestModel(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self):
        return self.title