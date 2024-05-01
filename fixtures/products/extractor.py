import json
import os
import requests

def download_images(json_data, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for product in json_data:
        if 'images' in product:
            product_id = str(product['id'])
            product_folder = os.path.join(download_folder, f"product-images/{product_id}")
            if not os.path.exists(product_folder):
                os.makedirs(product_folder)

            for image_url in product['images']:
                # Extract the filename from the image URL
                filename = os.path.basename(image_url)
                # Combine the product folder path and filename
                filepath = os.path.join(product_folder, filename)
                # Check if the file already exists
                if os.path.exists(filepath):
                    print(f"Skipping download: {filepath} - File already exists")
                else:
                    # Download the image
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        with open(filepath, 'wb') as f:
                            f.write(response.content)
                        print(f"Downloaded: {filepath}")
                    else:
                        print(f"Failed to download: {image_url}")

# Load JSON data from file
with open('products.json', 'r') as file:
    json_data = json.load(file)

# Define the folder where you want to save the images
download_folder = 'downloaded_images'

# Download images
download_images(json_data, download_folder)

