from django.contrib import admin
from . models import Page



# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields =('created_at','updated_at')
    search_fields = ('title', 'content')
    list_filter =('visible',)

    
admin.site.register(Page)


# configuracion del panel 
title = "proyecto Django"
subtitle = "Panel de gestion"


admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title =subtitle