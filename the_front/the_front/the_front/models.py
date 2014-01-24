from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime

class News(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  text = models.TextField(blank=True, null=True, default="")
  date = models.DateField(_("Date"), default=datetime.date.today)
  is_archived = models.BooleanField(default=False)

  def __unicode__(self):
    return "%s (%s)" % (self.name, self.date)

