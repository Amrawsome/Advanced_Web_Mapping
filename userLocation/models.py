from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    location = models.PointField(editable=False,blank=True,null=True,default=None)

    def __str__(self):
        return str(self.lon), str(self.lat)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class parkingSpot(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    location = models.PointField(editable=False,blank=True,null=True,default=None)
    lon = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    def __str__(self):
        return str(self.location),str(self.lon),str(self.lat)


@receiver(post_save, sender=User)
def create_user_parkingspot(sender, instance, created, **kwargs):
    if created:
        parkingSpot.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_parkingspot(sender, instance, **kwargs):
    instance.parkingspot.save()


