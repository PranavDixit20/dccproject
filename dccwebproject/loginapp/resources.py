from import_export import resources
from .models import engg,Customer,coadmin,callallocate,stock,products

class EnggResource(resources.ModelResource):
    class Meta:
        model = engg

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer

class CoadminResource(resources.ModelResource):
    class Meta:
        model = coadmin

class CallallocateResource(resources.ModelResource):
    class Meta:
        model = callallocate

class StockResource(resources.ModelResource):
    class Meta:
        model = stock

class ProductResource(resources.ModelResource):
    class Meta:
        model = products
