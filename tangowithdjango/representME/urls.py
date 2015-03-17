from django.conf.urls import patterns, url
from representME import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #url(r'^user/(?P<username>[\w\-]+)/$', views.userview, name='user'),
        #url(r'^about/$', views.about, name='about'),
        #url(r'^add_category/$', views.add_category, name='add_category'),
        #url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        #url(r'^register/$', views.register, name='register'),
        #url(r'^login/$', views.user_login, name='login'),
        #url(r'^restricted/$', views.restricted, name='restricted'),
        #url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^laws/$', views.laws, name='laws'),
        url(r'^laws/(?P<law_name>[\w\-.]+)/$', views.law, name='law'),
        url(r'^msps/$', views.msps, name='msps'),
        url(r'^logout/$', views.user_logout, name='logout'),
		url(r'^search/$', views.search, name='search'),
)