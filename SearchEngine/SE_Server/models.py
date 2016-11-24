# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField('User Name', max_length=30)
    password = models.CharField('Password', max_length=30)
    
    def __unicode__(self):
        return self.username
    
class DirectoryInfo(models.Model):
    dirname = models.CharField('Directory Name', max_length=100)
    createtime = models.DateTimeField('Start Time')
    finishtime = models.DateTimeField('Finish Time')
    
    def __unicode__(self):
        return self.dirname
    
class FileInfo(models.Model):
    dirinfo = models.ForeignKey(DirectoryInfo)
    filepath = models.FilePathField('File Path')
    filename = models.CharField('File Name', max_length=80)
    fileflag = models.IntegerField('Status(0-2)', default=0)
    filesize = models.BigIntegerField('File Size')
    createtime = models.DateTimeField('Start Time')
    finishtime = models.DateTimeField('Finish Time')
    
    def __unicode__(self):
        return self.filename