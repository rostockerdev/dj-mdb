from django.contrib import admin

from postgresapp.models import POSTGRESModel

class POSTGRESAdminArea(admin.AdminSite):
    
    site_header = 'POSTGRES Admin'
    site_title = 'Postgres Admin Interface'

postgres_site = POSTGRESAdminArea(name='POSTGRESAdmin')

postgres_site.register(POSTGRESModel)
admin.site.register(POSTGRESModel)
