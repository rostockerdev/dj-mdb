from django.contrib import admin

from mysqlapp.models import MYSQLModel

class MYSQLAdminArea(admin.AdminSite):

    # admin.site.index_title = "Mysql Administration"
    site_header = "Mysql Admin"
    site_title = "Mysql Admin Interface"

mysql_site = MYSQLAdminArea(name="MYSQLAdmin")
mysql_site.register(MYSQLModel)
admin.site.register(MYSQLModel)
