from rest_framework import serializers
from .models import Vps


class VpsMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vps
        fields = '__all__'

    def create(self, validated_data):
        return Vps.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class VpsFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vps
        fields = '__all__'
        extra_kwargs = {
          'cpu': {'required': False},
          'ram': {'required': False},
          'hdd': {'required': False},
          'status': {'required': False},
        }
