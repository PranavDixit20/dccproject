from import_export import resources
from .models import engg

class EnggResource(resources.ModelResource):
    class Meta:
        model = engg
