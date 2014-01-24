from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User

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

class ArtistMedia(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  artist = models.ForeignKey(Artist)
  video_link = models.CharField(max_length=255, blank=True, null=True, default="")
  image = models.ImageField(upload_to='artist_media/', default="", null=True, blank=True, editable=False)
  thumbnail = models.ImageField(upload_to='artist_media/', default="", null=True, blank=True, editable=False)
  full_res_image = models.ImageField(upload_to='artist_media/', default="", null=True, blank=True)
  is_default_image = models.BooleanField(default=False)

  def __unicode__(self):
    return self.name

  def thumb(self):
    return "%s%s" % (settings.MEDIA_URL, self.thumbnail.name)

  def save(self):
    super(ArtistMedia, self).save()
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
    super(ArtistMedia, self).save()

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
    super(ArtistMedia, self).save()

