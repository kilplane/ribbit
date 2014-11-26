from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'ribbit.ribbit_app.views.index'),                # root
    url(r'^admin/', include(admin.site.urls)),                  # admin
    url(r'^login$', 'ribbit.ribbit_app.views.login_view'),      # login
    url(r'^logout$', 'ribbit.ribbit_app.views.logout_view'),    # logout
    url(r'^signup$', 'ribbit.ribbit_app.views.signup'),         # signup
    url(r'^submit$', 'ribbit.ribbit_app.views.submit'),         # submit new ribbit
    url(r'^users/$', 'ribbit.ribbit_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'ribbit.ribbit_app.views.users'),
    url(r'^follow$', 'ribbit.ribbit_app.views.follow'),
    url(r'^ribbits$', 'ribbit.ribbit_app.views.index'),         # Link oli aga tutorialsis urli selle peale ei olnud... Go figure.. 
)