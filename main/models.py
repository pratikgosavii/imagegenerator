from django.db import models

# Create your models here.



from datetime import datetime, timezone

class theme(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/theme', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title
