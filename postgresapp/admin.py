from django.contrib import admin

from postgresapp.models import POSTGRESModel

class POSTGRESAdminArea(admin.AdminSite):
    
    site_header = 'POSTGRES Admin'
    site_title = 'Postgres Admin Interface'

class POSTGRESModelAdmin(admin.ModelAdmin):

    fields = ['id', 'title', 'content']



postgres_site = POSTGRESAdminArea(name='POSTGRESAdmin')

postgres_site.register(POSTGRESModel, POSTGRESModelAdmin)
admin.site.register(POSTGRESModel, POSTGRESModelAdmin)
