from django.contrib import admin
from django.urls import path

from mysqlapp.admin import mysql_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysqladmin/', mysql_site.urls),
]

## MYSQL Admin Interface

# admin.site.index_title = "Mysql Administration"
# admin.site.site_header = "Mysql Admin"
# admin.site.site_title = "Mysql Admin Interface"