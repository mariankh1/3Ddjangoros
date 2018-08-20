from django.db import models

# Create your models here.
class Drone(models.Model):
    drone_name = models.CharField(max_length=100)
    drone_id = models.IntegerField()
    added_date = models.DateTimeField()
    def __str__(self):
        return self.drone_name

class DroneMission(models.Model):
    mission_name= models.CharField(max_length=200)
    added_date = models.DateTimeField()
    def __str__(self):
        return self.mission_name
