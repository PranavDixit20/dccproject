from rest_framework import serializers
from . models import callallocate,engg

class CallAllocateSerializer(serializers.ModelSerializer):

    class Meta:
        model = callallocate
        fields = '__all__'

class EnggSerializer(serializers.ModelSerializer):

    class Meta:
        model = engg
        fields = '__all__'

class EventCallSerializer(serializers.ModelSerializer):

    class Meta:
        model = callallocate
        fields = [
        'id',
        'title',
        'start',
        'end',
        'description',
        ]
