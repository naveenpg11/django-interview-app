# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings



class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    uname = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {uname}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b  %m, %Y, %H:%M %p')
    
    def as_dict(self):
        return {'uname': self.uname, 'message': self.message, 'timestamp': str(self.formatted_timestamp)}

class Status(models.Model):
    uname = models.TextField()
    room = models.TextField()