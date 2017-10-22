from django.shortcuts import render
from django.http import HttpResponse

import logging
import os

def index(request):
    # now = datetime.datetime.now()
    logger = logging.getLogger(__name__)
    logger.debug('index view called')

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # url="/rango/"
    # html = "<html><body>Rango says here is the about page. <br/> <a href='%s'>Index</a> </body></html>" % url
    # return HttpResponse(html)
    return render(request, 'rango/about.html')
