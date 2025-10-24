import os

def compare_dirs(dir1, dir2):
    files1 = []
    files2 = []

    for root, dirs, files in os.walk(dir1):
        for file in files:
            full_path = os.path.join(root, file)
            files1.append(full_path)

    for root, dirs, files in os.walk(dir2):
        for file in files:
            full_path = os.path.join(root, file)
            files2.append(full_path)

    only_in_dir1 = [f for f in files1 if f not in files2]
    only_in_dir2 = [f for f in files2 if f not in files1]

    print("Только в", dir1)
    for file in only_in_dir1:
        print(file)

    print("\nТолько в", dir2)
    for file in only_in_dir2:
        print(file)

if __name__ == "__main__":
    dir1 = input("Введите первую директорию: ")
    dir2 = input("Введите вторую директорию: ")

    compare_dirs(dir1, dir2)