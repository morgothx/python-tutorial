from rest_framework import serializers
from .models import Serie
from .models import Ethnics

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')

class EthnicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnics
        fields = ('id', 'name', 'description')
