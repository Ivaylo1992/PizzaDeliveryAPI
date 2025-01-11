from .models import Order
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('size', 'quantity')


class OrderDetailSerializer(OrderCreationSerializer):
    class Meta(OrderCreationSerializer.Meta):
        fields = ('size', 'status', 'quantity', 'created_at', 'updated_at')