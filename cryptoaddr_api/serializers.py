from rest_framework import serializers
from .models import Cryptoaddress

class CryptoaddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cryptoaddress
        fields = '__all__'