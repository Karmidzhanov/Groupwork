from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mealsignups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('signup/')), #referred to as signup:index in template
    url(r'^signup/', include('signup.urls', namespace="signup")),
    url(r'^admin/', include(admin.site.urls)),
)

