from rest_framework import serializers
from api.models import FundsEstate

class FundsEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundsEstate
        fields = '__all__'