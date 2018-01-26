# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    DOG_SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    user = models.OneToOneField(
        User,
        related_name='dog_profile',
        on_delete=models.CASCADE
    )
    dog_name = models.CharField(max_length=32)
    first_name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        default="First Name"
    )
    last_name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        default="Last Name"
    )
    profile_pic = models.ImageField(upload_to='profile/%Y/%m/%d')
    phone_number = models.CharField(
        max_length=10,
        default='XXX-XXX-XXXX'
    )
    license_id = models.CharField(
        max_length=7,
        blank=False,
        null=False,
        default="XXXXXXX"
    )
    owner_address = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        default="Address"
    )
    payment_date = models.DateTimeField(
        default=datetime.now
    )
    years_issued = models.IntegerField(
        default=0
    )
    dog_sex_choices = models.CharField(
        max_length=6,
        choices=DOG_SEX_CHOICES,
        default=MALE,
    )
    neutered = models.BooleanField(
        default=False
    )

    def __unicode__(self):
          return "%s %s" % (self.user.first_name, self.user.last_name)

    def __str__(self):
          return "%s %s" % (self.user.first_name, self.user.last_name)