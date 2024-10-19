from django.db import models

# Create your models here.

class Cities(models.Models):
    id_city = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name
    
class Places(models.Models):
    id_place = models.IntegerField(primary_key=True)
    place_name = models.CharField(max_length=250)
    id_city = models.ForeignKey(Cities.id_city)
    addres = models.CharField(max_length=250)
    coordinates = models.CharField(max_length=250)

    def __str__(self):
        return self.place_name
