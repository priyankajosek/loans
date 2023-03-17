from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loan
        fields = ['loan_amount','interest','tenure']

    def validate(self,attrs):
        loan_amount = attrs.get('loan_amount',0)
        interest = attrs.get('interest',0)
        tenure = attrs.get('tenure',0)
        if loan_amount <= 0 or interest <= 0 or tenure <= 0:
            raise serializers.ValidationError(
                {'loan|interest|tenure':'Please provide positive values'})
        return super().validate(attrs)

    def create(self,validated_data):
        return Loan.objects.create(**validated_data)