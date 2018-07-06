from rest_framework import serializers
from django.contrib.auth.models import User
from . models import callallocate,engg,customer

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
        'call_alloc_time',
        'end',
        'description',
        ]

class ChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = customer
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
