from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'order', 'provider', 'amount', 'status', 'transaction_id', 'created_at',]
        read_only_fields = ['status', 'created_at',]
