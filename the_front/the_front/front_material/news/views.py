from django.shortcuts import render_to_response, redirect
#from django.http import Http404
from django.conf import settings
from django.core.context_processors import csrf
from front_material.models import NewsArticle, NewsMedia
from the_front.views import common_args

def home(req):
  args = common_args(req)
  args['news'] = NewsArticle.objects.all()
  return render_to_response("news/list.jade", args)

def news(req, pk):
  args = common_args(req)
  news = NewsArticle.objects.get(pk=pk)
  if not news:
    args['error'] = 'No news found'
    return render_to_response("error.jade", args)
  args['news'] = news
  args['news_images'] = NewsMedia.objects.filter(news_article=news)
  return render_to_response("news/show.jade", args)