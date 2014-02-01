from pyquery import PyQuery
import urllib
from front_material.models import *
from datetime import datetime

def doTheDamnThing():
  base = "http://www.nolafront.org/pages/"
  
  req = urllib.urlopen('%sarchive.htm' % base)
  html = req.read()
  pq = PyQuery(html)
  
  ass = pq("a.style2")
  
  a_iter = ass.items()
  a = a_iter.next()
  count = 0
  last_year = "2013"
  while count < len(ass) - 1:
    href = "%s%s" % ( base, a.attr('href') )
    name = a.text()
    if len(name) > 100:
      name = name[:14]
    artists_info = a.parent().text()
    artists_info = artists_info[len(name)+1:]
    print href
    nq = PyQuery(href)
    imgs = nq.find('img')
    n_iter = imgs.items()
    img = n_iter.next()
    text = ""
    i = 0
    while i < len(imgs) - 1:
      i += 1
      try:
        img = n_iter.next()
        src = img.attr('src')
        img.attr('src', "%s%s" % (base, src))
      except:
        break
    kids = nq.find('div#Content').children()
    n_iter = kids.items()
    n_iter.next()
    n_iter.next()
    text = ""
    i = 0
    while i < len(kids) - 1:
      i += 1
      try:
        text += n_iter.next().html()
      except:
        break
    news, created = NewsArticle.objects.get_or_create(name=name)
    #if created:
      #print 'its news! haha get it!!'
    #else:
      #print 'OLD!!!!'
    news.name = name
    news.artists_info = artists_info
    news.name = name
    news.text = text
    date = name.split('-')
    try:
      date = datetime.strptime(date[1], "%B %d, %Y")
      last_year = date.year
    except:
      try:
        date = "%s, %s" % (date[1], last_year)
        date = datetime.strptime(date, "%B %d, %Y")
      except:
        date = datetime.strptime(last_year, "%Y")
    news.date = date
    news.save()
    count += 1
    a = a_iter.next()
  
  #href = archive[0]['href']
  #name = archive[0]['name']
  #text = archive[0]['text']
  #print text
  
  '''
  lines = req.readlines()
  ass = []
  for line in lines:
    try:
      line.index('<a')
      ass.append(line)
    except:
      continue
  
  links = []
  ass.pop(0)
  for a in ass:
    start = a.index('href="')
    end = a.index('.htm"')
    links.append("%s%s" % (base, a[start:end]))
  '''
