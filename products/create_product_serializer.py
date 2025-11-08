from rest_framework import serializers
from products.models import Product

class createProductSerializer(serializers.ModelSerializer):
    # name  = serializers.CharField(max_length=100)
    # price = serializers.FloatField()

    class Meta:
        model = Product
        fields = ("id","name", "price", "stock", "category")
        read_only_fields = ("id",)
