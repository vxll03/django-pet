from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=50)


class Note(models.Model):
    title = models.CharField(max_length=50)
    test = models.ForeignKey("Test", related_name='notes', on_delete=models.SET_NULL, blank=True, null=True)