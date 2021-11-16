from django import contrib
from django.contrib import admin
from django.contrib.auth.views import LoginView , LogoutView
from django.urls import path, include
from leads.views import landingPageView , signupView #landning_page

from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingPageView.as_view() , name='landing_page'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('signup/', signupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
    ]





admin.site.site_header = 'CRM ADMIN'
admin.site.site_title = 'CRM'
admin.site.index_title = 'CRM ADMIN'
admin.site.site_url = None

