from rest_framework import serializers
from ..models.chart_of_account import ChartOfAccount

class ChartOfAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = '__all__'