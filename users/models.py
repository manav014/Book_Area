from django.db import models


# Create your models here.

class Users(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=300)
    user_contact = models.CharField(max_length=10)