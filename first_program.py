import os
import hashlib

def calculate_image_hash(image_path):
    """
    Вычисляет хеш изображения.
    """
    with open(image_path, 'rb') as f:
        image_data = f.read()
        return hashlib.md5(image_data).hexdigest()

def find_duplicate_images(folder_path):
    """
    Ищет дубликаты изображений в указанной папке.
    """
    image_hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            image_path = os.path.join(root, file)
            image_hash = calculate_image_hash(image_path)

            if image_hash in image_hashes:
                # Найден дубликат
                duplicates.append((image_path, image_hashes[image_hash]))
            else:
                image_hashes[image_hash] = image_path

    return duplicates

if __name__ == "__main__":
    folder_to_search = "/путь/к/папке/с/изображениями"
    duplicate_pairs = find_duplicate_images(folder_to_search)

    if duplicate_pairs:
        print("Найдены дубликаты:")
        for image1, image2 in duplicate_pairs:
            print(f"{image1} и {image2}")
    else:
        print("Дубликатов не найдено.")
