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

  def __unicode__(self):
    return self.name

  def save(self):
    super(Artist, self).save()
    self.slug = slugify(self.name)
    super(Artist, self).save()

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

