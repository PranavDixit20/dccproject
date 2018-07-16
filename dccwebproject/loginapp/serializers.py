from rest_framework import serializers
from django.contrib.auth.models import User
from . models import callallocate,engg,customer
from . models import Message


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']


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
