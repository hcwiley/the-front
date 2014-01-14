from django.shortcuts import render_to_response, redirect
#from django.http import Http404
from django.conf import settings
from django.core.context_processors import csrf

def common_args(request):
    """
    The common arguments for all gallery views.
    
    STATIC_URL: static url from settings
    """ 
    user = request.user if request.user.is_authenticated() else None
    args = {
                'STATIC_URL' : settings.STATIC_URL,
                'MEDIA_URL' : settings.MEDIA_URL,
                'user' : user,
                'PAGE_TITLE' : 'The Front',
           }
    args.update(csrf(request))
    return args

def home(req):
  args = common_args(req)
  return render_to_response("index.jade", args)
  
def contact(req):
  args = common_args(req)
  return render_to_response("contact.jade", args)
  
def about(req):
  args = common_args(req)
  return render_to_response("about.jade", args)
  
