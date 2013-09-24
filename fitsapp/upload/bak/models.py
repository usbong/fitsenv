# -*- coding: utf-8 -*-
from django.db import models
from allauth import app_settings

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    uploader = models.ForeignKey(app_settings.USER_MODEL)
    description = models.CharField(max_length=300)
    date_uploaded = models.DateField(auto_now_add=True)

class DownloadCount(models.Model):
    document_id = models.ForeignKey('Document')
    count = models.IntegerField(default=0, blank=False, null=False)
