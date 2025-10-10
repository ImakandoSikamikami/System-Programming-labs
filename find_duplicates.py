import os
import hashlib
from dotenv import load_dotenv

load_dotenv()

def get_file_hash(file_path, block_size=65536):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buf = file.read(block_size)
        while buf:
            hasher.update(buf)
            buf = file.read(block_size)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    file_hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                file_hash = get_file_hash(file_path)
                if file_hash in file_hashes:
                    duplicates.append((file_hashes[file_hash], file_path))
                else:
                    file_hashes[file_hash] = file_path
            except (PermissionError, FileNotFoundError):
                continue

    return duplicates

if __name__ == "__main__":
    # Get directory path from environment variable
    target_directory = os.getenv("TARGET_DIRECTORY", ".")

    print(f"Scanning directory: {target_directory}\n")
    duplicates = find_duplicate_files(target_directory)

    if duplicates:
        print("Duplicate files found:")
        for original, duplicate in duplicates:
            print(f"Original: {original}")
            print(f"Duplicate: {duplicate}\n")
    else:
        print("No duplicate files found.")