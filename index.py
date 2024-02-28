import os
import sys
from PIL import Image

def convert_image_to_webp(image_path, output_folder):
    try:
        im = Image.open(image_path)
        if im.format == "WEBP":
            # Skip if already in WEBP format
            return
        im = im.convert("RGB")
        filename = os.path.basename(image_path)
        print(filename)
        print("filename")
        output_path = os.path.join(output_folder, filename.split('.')[0] + ".webp")
        im.save(output_path, "WEBP", quality=100)
        print(f"Converted {image_path} to WEBP")
    except Exception as e:
        print(f"Failed to convert {image_path}: {e}")

def convert_folder_to_webp(folder_path):
    output_folder = os.path.join(os.path.dirname(folder_path), os.path.basename(folder_path) + "_converted")
    try:
        os.makedirs(output_folder, exist_ok=False)
    except:
        for i in range(1, 100):
            output_folder = os.path.join(os.path.dirname(folder_path), os.path.basename(folder_path) + "_converted" + f"({i})")
            try:
                os.makedirs(output_folder, exist_ok=False)
                break
            except:
                continue
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                convert_image_to_webp(image_path, output_folder)

def main():
    if len(sys.argv) < 2:
        print("No path provided")
        return

    path = sys.argv[1]
    if os.path.isdir(path):
        convert_folder_to_webp(path)
    elif os.path.isfile(path):
        print("file ")
        os.makedirs("converted", exist_ok=True)
        convert_image_to_webp(path, "converted")
    else:
        print("Invalid path provided")

if __name__ == "__main__":
    main()
