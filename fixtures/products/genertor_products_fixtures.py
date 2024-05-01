# dummy_products

import json
import os

# Read categories fixture data from categories_fixtures.json
with open('categories_fixtures.json', 'r') as file:
    categories_fixtures = json.load(file)

# Create a mapping of category names to primary keys
category_pk_mapping = {category['fields']['name']: category['pk'] for category in categories_fixtures}

# Read products from products.json
with open('products.json', 'r') as file:
    products = json.load(file)

# Define the directory where images and thumbnails are downloaded
download_folder = 'downloaded_images'

# Create fixtures data
products_fixtures = []

# Create fixtures data
images_fixtures = {}

pk = 1  # Start primary key from 1

for product in products:
    product_id = product['id']
    product_images = []

    for image_path in product['images']:
        # Extract product ID from the image path
        _, img_path = image_path.split("https://cdn.dummyjson.com/product-images/")
        x = f'product_images/{img_path}'

        # Add image fixture
        product_images.append(pk)
        pk += 1

    images_fixtures[f"{product_id}"] = product_images

pr_pk = 1

for product in products:
    product_id = product['id']
    product_images = images_fixtures[f"{product_id}"]
    category_id = category_pk_mapping.get(product['category'])
    if category_id is not None:

        # Add product fixture
        products_fixtures.append({
            "model": "dummy_products.Product",  # Replace 'your_app_name' with your Django app's name
            "pk": product_id,
            "fields": {
                "title": product['title'],
                "description": product['description'],
                "price": float(product['price']),
                "discount_percentage": float(product['discountPercentage']),
                "rating": float(product['rating']),
                "stock": product['stock'],
                "brand": product['brand'],
                "category": category_id,
                "thumbnail_image": os.path.join('product_images', str(product_id), 'thumbnail.jpg'),
                "images": product_images
            }
        })

        pr_pk += 1


# Write fixtures data to products_fixtures.json
with open('products_fixtures.json', 'w') as outfile:
    json.dump(products_fixtures, outfile, indent=4)

# # Write image fixtures data to images_fixtures.json
# with open('ximages_fixtures.json', 'w') as outfile:
#     json.dump(images_fixtures, outfile, indent=4)
