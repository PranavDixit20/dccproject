from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import callallocate,coadmin,customer,engg,callallocate,stock,products
from . models import Chat

admin.site.register(Chat)




@admin.register(products)
class ProductsAdmin(ImportExportModelAdmin):
    pass

@admin.register(engg)
class EnggAdmin(ImportExportModelAdmin):
    pass

@admin.register(customer)
class CustomerAdmin(ImportExportModelAdmin):
    pass

@admin.register(coadmin)
class CoadAdmin(ImportExportModelAdmin):
    pass

@admin.register(callallocate)
class CallallocateAdmin(ImportExportModelAdmin):
    pass

@admin.register(stock)
class StockAdmin(ImportExportModelAdmin):
    pass
