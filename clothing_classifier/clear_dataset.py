import os
import csv

DATA_FOLDER = 'data'
IMAGES_CSV = os.path.join(DATA_FOLDER, 'images.csv')
IMAGES_COMPRESSED_FOLDER = os.path.join(DATA_FOLDER, 'images_compressed')
MISSING_IMAGES_FILE = os.path.join(DATA_FOLDER, 'missing_images.txt')

missing_images = []

with open(IMAGES_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not row:
            continue
        image_name = row[0].strip() + ".jpg"
        image_path = os.path.join(IMAGES_COMPRESSED_FOLDER, image_name)

        if not os.path.isfile(image_path):
            missing_images.append(image_name)

if missing_images:
    with open(MISSING_IMAGES_FILE, 'w', encoding='utf-8') as f:
        for name in missing_images:
            f.write(name + '\n')
    print(f"Missing images written to {MISSING_IMAGES_FILE}")
else:
    print("No missing images found.")