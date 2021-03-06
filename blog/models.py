from django.db import models
from datetime import date

# Create your models here.
class Blog(models.Model):
    sr_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title