from rest_framework import serializers
from . models import callallocate

class CallAllocateSerializer(serializers.ModelSerializer):

    class Meta:
        model = callallocate
        fields = '__all__'
