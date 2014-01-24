from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime

class FrontMedia(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  video_link = models.CharField(max_length=255, blank=True, null=True, default="")
  image = models.ImageField(upload_to='news_media/', default="", null=True, blank=True, editable=False)
  thumbnail = models.ImageField(upload_to='news_media/', default="", null=True, blank=True, editable=False)
  full_res_image = models.ImageField(upload_to='news_media/', default="", null=False, blank=False)
  is_default_image = models.BooleanField(default=False)

  def __unicode__(self):
    return self.name

  def thumb(self):
    return "%s%s" % (settings.MEDIA_URL, self.thumbnail.name)

  def save(self):
    super(FrontMedia, self).save()
    self.saveImage()
    self.saveThumbnail()

  def saveImage(self):
    import Image
    path = self.full_res_image.path
    image = Image.open(path)
    r = float(image.size[1])/float(image.size[0])
    image = image.resize((900, int(900*r)), Image.ANTIALIAS)
    path = path.split(".")
    path = "%s-small.%s" % (path[0], path[1])
    image.save(path)
    path = path.split(settings.MEDIA_ROOT)
    self.image = "%s" % (path[1])
    super(FrontMedia, self).save()

  def saveThumbnail(self):
    import Image
    path = self.full_res_image.path
    image = Image.open(path)
    r = float(image.size[1])/float(image.size[0])
    image = image.resize((150, int(150*r)), Image.ANTIALIAS)
    path = path.split(".")
    path = "%s-thumb.%s" % (path[0], path[1])
    image.save(path)
    path = path.split(settings.MEDIA_ROOT)
    self.thumbnail = "%s" % (path[1])
    super(FrontMedia, self).save()

class NewsArticle(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  text = models.TextField(blank=True, null=True, default="")
  date = models.DateField(default=datetime.date.today)
  is_archived = models.BooleanField(default=False)

  def __unicode__(self):
    return "%s (%s)" % (self.name, self.date)

  def thumb(self):
    image = self.newsmedia_set.filter(is_default_image=True)
    if len(image) == 0 :
      image = self.newsmedia_set.all()
    if len(image) == 0 :
      return ""
    image = image[0]
    return image.thumb()

  def get_absolute_url(self):
    return "/news/%s-%s" % (self.date, self.pk)

class NewsMedia(FrontMedia):
  news_article = models.ForeignKey(NewsArticle)
