from django.conf.urls import url
from rango import views

urlpatterns = [
    # match empty string only
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
]
