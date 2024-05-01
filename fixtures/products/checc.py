import os

def has_image_files(directory, filename):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.webp']
    for root, _, files in os.walk(directory):
        for file in files:
            name, extension = os.path.splitext(file)
            if name.lower() == filename.lower() and extension.lower() in image_extensions:
                return True
    return False

def check_folders(directory):
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not has_image_files(dir_path, "thumbnail"):
                print(f"The folder {dir_path} does not contain an image file named 'thumbnail'.")

if __name__ == "__main__":
    product_images_directory = "product_images"
    check_folders(product_images_directory)
