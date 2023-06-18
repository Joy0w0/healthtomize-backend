from django.contrib import admin
from django.urls import path, include
import sys


sys.path.append('/usr/lib/python3/dist-packages')
urlpatterns = [
    path('', include('apps.url')),
]

admin.site.site_header = '관리자 페이지'
admin.site.site_title = 'Healthtomize'



