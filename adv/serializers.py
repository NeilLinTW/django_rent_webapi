from rest_framework import serializers
from adv.models import Advertisement, RateHistory

class AdvSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'Id',
            'City',
            'Town',
            'Addr',
            'Body',
            'Image1',
            'Image2',
            'CreateDate',
            'ModifyDate',
            'IsEnable',
            'IsPay',
            "IP"
            
        )
        model = Advertisement



class RateSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'Id',
            'IPAddr',
            'Val',
            'CreateDate',
        )
        model = RateHistory