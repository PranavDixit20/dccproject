from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import callallocate,coadmin,customer,engg,Room

admin.site.register(callallocate)
admin.site.register(coadmin)
admin.site.register(customer)
#admin.site.register(engg)

@admin.register(engg)
class EnggAdmin(ImportExportModelAdmin):
    pass

admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)
