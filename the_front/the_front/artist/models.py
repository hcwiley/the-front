from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from front_material.models import FrontMedia

# Create your models here.

class Artist(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  slug = models.CharField(max_length=100, blank=True, null=True, default="", editable=False)
  bio = models.TextField(blank=True, null=True, default="")
  artist_statement = models.TextField(blank=True, null=True, default="")
  user = models.ForeignKey(User)
  website = models.CharField(max_length=100, blank=True, null=True, default="")
  email = models.CharField(max_length=100, blank=True, null=True, default="")
  cv = models.FileField(upload_to='front_media/', blank=True, null=True, default="")

  class Meta:
    ordering = ['name']
  
  def __unicode__(self):
    return self.name

  def save(self):
    super(Artist, self).save()
    self.slug = slugify(self.name)
    super(Artist, self).save()

  def cv_link(self):
    return "%s%s" % (settings.MEDIA_URL, self.cv.name)

  def cv_name(self):
    if self.cv:
      return "%s-CV%s" % (self.name, self.cv.name[self.cv.name.rindex("."):])
    else:
      return ""

  def web(self):
    if self.website.count("http") > 0:
      return self.website
    else:
      return "http://%s" % self.website

  def thumb(self):
    image = self.artistmedia_set.filter(is_default_image=True)
    if len(image) == 0 :
      image = self.artistmedia_set.all()
    if len(image) == 0 :
      return ""
    image = image[0]
    return image.thumb()

  def get_absolute_url(self):
    return "/artists/%s" % (self.slug)

class ArtistMedia(FrontMedia):
  artist = models.ForeignKey(Artist)
  dimensions = models.CharField(max_length=100, blank=False, null=False, default="")
  medium = models.CharField(max_length=100, blank=False, null=False, default="")
  year = models.CharField(max_length=4, blank=False, null=False, default="")

