from rest_framework import serializers
from .models import Serie
from .models import Ethnic
from .models import Service

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')

class EthnicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnic
        fields = ('id', 'name', 'description')

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'description', 'type')

class FiltersSerializer(serializers.ModelSerializer):
    services = ServicesSerializer(many=True)
    ethnics = EthnicsSerializer(many=True)
