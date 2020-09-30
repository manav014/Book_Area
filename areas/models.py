from django.db import models


# Create your models here.


class Areas(models.Model):
    Area_id = models.AutoField
    Area_college = models.CharField(max_length=100)
    Area_name = models.CharField(max_length=100)
    Area_email = models.EmailField(default="")
    Area_price = models.IntegerField(default=0)
    Area_desc = models.CharField(max_length=500, default="")
    Area_image = models.ImageField(upload_to="areas/images", default="")

    def __str__(self):
        return self.Area_name
