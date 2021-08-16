from django.db import models
#Crime Database Schema
class Crime(models.Model):
    type = models.CharField(max_length=100)
    year = models.IntegerField()
    month= models.IntegerField()
    day= models.IntegerField()
    hour=models.IntegerField()
    minute=models.IntegerField()
    block=models.CharField(max_length=100)
    neighborhood=models.CharField(max_length=100)
    x_coordinate=models.DecimalField(max_digits=50,decimal_places=4)
    y_coodinate=models.DecimalField(max_digits=50,decimal_places=4)

  
    def __str__(self):
        return self.type

