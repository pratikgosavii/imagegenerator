from django.db import models
from datetime import datetime, timezone

from django.contrib.auth.models import User



class user_details(models.Model):
    
    user = models.ForeignKey(User, related_name="related_user", on_delete=models.CASCADE)
    mobile_no = models.IntegerField()
    avatar = models.ImageField(upload_to='static/user/', blank=False, null=False, height_field=None, width_field=None, max_length=None)
    