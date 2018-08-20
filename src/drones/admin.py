from django.contrib import admin

# Register your models here.
from .models import Drone
from .models import DroneMission
admin.site.register(Drone)
admin.site.register(DroneMission)
