from django.conf.urls import patterns, include, url
from django.contrib import admin

from users import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rethink_auth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', views.my_view),

    url(r'^admin/', include(admin.site.urls)),
)
