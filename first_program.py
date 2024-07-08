import os
import hashlib

def calculate_image_hash(image_path):
    """
    Calculates the hash of the image.
    """
    if not isinstance(image_path, str) or not os.path.isfile(image_path):
        print(f"Error: {image_path} is not a valid file path.")
        return None

    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
            return hashlib.md5(image_data).hexdigest()
    except FileNotFoundError:
        print(f"Error: {image_path} does not exist.")
        return None
    except IOError:
        print(f"Error: Could not read the file at {image_path}.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred while processing {image_path}: {str(e)}")
        return None

def find_duplicate_images(folder_path):
    """
    Searches for duplicate images in the specified folder.
    """
    if not isinstance(folder_path, str) or not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory path.")
        return []

    image_hashes = set()
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            image_path = os.path.join(root, file)
            image_hash = calculate_image_hash(image_path)

            if image_hash is not None:
                if image_hash in image_hashes:
                    # Duplicate found
                    duplicates.append((image_path, image_hash))
                else:
                    image_hashes.add(image_hash)

    return duplicates

if __name__ == "__main__":
    folder_to_search = r"C:\Users\5\Desktop\photo"
    duplicate_pairs = find_duplicate_images(folder_to_search)

    if duplicate_pairs:
        print("Duplicates found:")
        for image1, image2 in duplicate_pairs:
            print(f"{image1} and {image2}")
    else:
        print("No duplicates found.")
