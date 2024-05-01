from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'image', 'rating', 'created_at', 'updated_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name
        return representation