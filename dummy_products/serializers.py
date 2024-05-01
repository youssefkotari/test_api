# serializers.py
from rest_framework import serializers
from .models import Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        images_data = self.context.get('request').data.getlist('images')
        product = Product.objects.create(**validated_data)
        for image_data in images_data:
            x = ProductImage.objects.create(image=image_data)
            product.images.add(x)
        return product

    def update(self, instance, validated_data):
        images_data = self.context.get('request').data.getlist('images')
        product = Product.objects.create(**validated_data)
        for image_data in images_data:
            x = ProductImage.objects.create(image=image_data)
            product.images.add(x)
        return product
