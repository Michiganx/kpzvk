from django.conf.urls import patterns, include, url
from django.contrib import admin




urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'kpz.views.index'),

    # url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    # url(r'^social/', include('social_auth.urls')),
    url(r'^login/$', 'kpz.views.login'),
    url(r'^disconnect/$', 'kpz.views.logout'),
    # url(r'^done/$', 'kpz.views.index',),
    url('', include('social.apps.django_app.urls', namespace='social')),

)
