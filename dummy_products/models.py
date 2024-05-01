from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    thumbnail_image = models.ImageField(upload_to='product_images')
    images = models.ManyToManyField('ProductImage', related_name='products')

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"Image {self.id}"


