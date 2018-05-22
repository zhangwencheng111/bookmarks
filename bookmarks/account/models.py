# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(null=True, blank=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
