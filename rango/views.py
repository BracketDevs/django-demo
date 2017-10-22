from django.shortcuts import render
from django.http import HttpResponse

import logging
import os

def index(request):
    # now = datetime.datetime.now()
    logger = logging.getLogger(__name__)
    logger.debug('index view called')

    url="/rango/about/"
    html = "<html><body>Rango says hey there partner! <br/> <a href='%s'>About</a> </body></html>" % url
    return HttpResponse(html)

def about(request):
    url="/rango/"
    html = "<html><body>Rango says here is the about page. <br/> <a href='%s'>Index</a> </body></html>" % url
    return HttpResponse(html)
