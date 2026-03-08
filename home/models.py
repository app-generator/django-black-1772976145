# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Item(models.Model):

    #__Item_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Item_FIELDS__END

    class Meta:
        verbose_name        = _("Item")
        verbose_name_plural = _("Item")


class Ressource(models.Model):

    #__Ressource_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)
    description2 = models.CharField(max_length=255, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    #__Ressource_FIELDS__END

    class Meta:
        verbose_name        = _("Ressource")
        verbose_name_plural = _("Ressource")


class Ressourcestat(models.Model):

    #__Ressourcestat_FIELDS__
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=True, blank=True)

    #__Ressourcestat_FIELDS__END

    class Meta:
        verbose_name        = _("Ressourcestat")
        verbose_name_plural = _("Ressourcestat")



#__MODELS__END
