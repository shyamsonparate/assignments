"""
Definition of urls for ContactManagerProject.
"""

from datetime import datetime
from django.conf.urls import url
from app.forms import BootstrapAuthenticationForm
from app.views import *
# Uncomment the next lines to enable the admin:
from django.conf.urls import include,url,patterns
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^display$', 'app.views.display', name='display'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^addContact', 'app.views.addContact', name='addContact'),
    url(r'^delete/(\d+)/$','app.views.delete'),
    url(r'^update/(\d+)/$','app.views.update',name='update'),
    url(r'^editToSave','app.views.editToSave',name='editToSave'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    ]