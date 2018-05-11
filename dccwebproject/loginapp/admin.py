from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import callallocate,coadmin,customer,engg

admin.site.register(callallocate)
admin.site.register(coadmin)
admin.site.register(customer)
#admin.site.register(engg)

@admin.register(engg)
class EnggAdmin(ImportExportModelAdmin):
    pass
