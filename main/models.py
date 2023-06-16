from django.db import models

# Create your models here.



from datetime import datetime, timezone



CATEGORY_CHOICES = (
    ("general", "general"),
    ("festival", "festival"),
    ("happy birthday", "happy birthday"),
    # ....
    ("invitation", "invitation"),
)



class theme(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/theme', height_field=None, width_field=None, max_length=None)
    category = models.CharField(max_length=50,
                    choices=CATEGORY_CHOICES,
                  default="general")
    


    def __str__(self):
        return self.title



