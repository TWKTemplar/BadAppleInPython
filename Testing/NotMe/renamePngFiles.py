import os


def rename_png_files():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]
    png_files.sort()  # Sort files by name

    for i, filename in enumerate(png_files):
        new_filename = f"{i}.png"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f"Renamed '{filename}' to '{new_filename}'")


rename_png_files()

