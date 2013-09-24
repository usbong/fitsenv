# -*- coding: utf-8 -*-
from django.db import models
from allauth import app_settings

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    uploader = models.ForeignKey(app_settings.USER_MODEL)
    description = models.CharField(max_length=300)
    date_uploaded = models.DateField(auto_now_add=True)
    download_count = models.PositiveIntegerField(max_length=10)
    up_vote = models.PositiveIntegerField(max_length=10)
    down_vote = models.PositiveIntegerField(max_length=10)
