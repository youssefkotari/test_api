# dummy_products

import json
import os

# Read products from products.json
with open('products.json', 'r') as file:
    products = json.load(file)

# Create fixtures data
images_fixtures = []

pk = 1  # Start primary key from 1

for product in products:
    product_id = product['id']
    product_images = []

    for image_path in product['images']:
        # Extract product ID from the image path
        _, img_path = image_path.split("https://cdn.dummyjson.com/product-images/")
        x = f'product_images/{img_path}'

        # Add image fixture
        images_fixtures.append({
            "model": "dummy_products.ProductImage",
            "pk": pk,
            "fields": {
                "image": x
            }
        })

        pk += 1

#
# # Write image fixtures data to images_fixtures.json
with open('images_fixtures.json', 'w') as outfile:
    json.dump(images_fixtures, outfile, indent=4)
