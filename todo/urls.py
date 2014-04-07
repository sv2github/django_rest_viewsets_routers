from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.views import task_router

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(task_router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
