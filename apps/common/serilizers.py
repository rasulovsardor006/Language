
from rest_framework import serializers
from apps.common.models import MainConfiguration, Country



class MainConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainConfiguration
        fields = ('app_store_url', 'play_market_url')
class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'ico_code', 'icon')