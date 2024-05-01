# dummy_products

import json

# Read categories from categories.json
with open('categories.json', 'r') as file:
    categories = json.load(file)

# Create fixtures data
fixtures_data = []
pk = 1  # Start primary key from 1
for category_name in categories:
    fixture = {
        "model": "dummy_products.Category",  # Replace 'your_app_name' with your Django app's name
        "pk": pk,
        "fields": {
            "name": category_name
        }
    }
    fixtures_data.append(fixture)
    pk += 1  # Increment primary key

# Write fixtures data to categories_fixtures.json
with open('categories_fixtures.json', 'w') as outfile:
    json.dump(fixtures_data, outfile, indent=4)
