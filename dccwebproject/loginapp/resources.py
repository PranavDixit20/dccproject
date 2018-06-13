from import_export import resources
from .models import engg,customer,coadmin,callallocate,stock

class EnggResource(resources.ModelResource):
    class Meta:
        model = engg

class CustomerResource(resources.ModelResource):
    class Meta:
        model = customer

class CoadminResource(resources.ModelResource):
    class Meta:
        model = coadmin

class CallallocateResource(resources.ModelResource):
    class Meta:
        model = callallocate

class StockResource(resources.ModelResource):
    class Meta:
        model = stock
