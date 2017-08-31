__author__ = 'Rushil'

from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

#ParticlesForm

urlpatterns = [
    url(r'^$', views.index, name = 'Index'),
    url(r'^alert/$', views.alert, name = 'Alert'),
    url(r'^map/$', views.disp_map, name = 'Map'),
    url(r'^register/$', views.register, name = 'Register'),
    url(r'^reg/$', views.home, name = 'Reg'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

