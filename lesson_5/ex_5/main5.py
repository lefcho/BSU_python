import os


def create_files_and_folder():
    folder_name = "install"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    try:
        with open("filenames.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            filename = line.strip()
            if filename:
                full_path = os.path.join(folder_name, f"{filename}.txt")
                with open(full_path, "w", encoding="utf-8") as new_file:
                    new_file.write("")

        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder_name):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.isfile(fp):
                    total_size += os.path.getsize(fp)

        size_mb = total_size / (1024 * 1024)
        print(f"Размер на папката '{folder_name}': {size_mb:.6f} MB")

    except FileNotFoundError:
        print("Файлът filenames.txt не беше намерен.")
