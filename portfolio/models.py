from django.db import models


# Create your models here.
class Portfolio(models.Model):
    sr_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    