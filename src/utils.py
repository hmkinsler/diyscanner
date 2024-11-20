import os

def rename_files(directory, prefix):
    """Renames all files in a directory with a given prefix."""
    for i, filename in enumerate(sorted(os.listdir(directory))):
        new_name = f"{prefix}_{i+1:03d}.jpg"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"Renamed {filename} to {new_name}")
