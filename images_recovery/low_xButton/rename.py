import os

# Set the directory where your .png files are located
directory = r'C:\Users\Guraspy\Desktop\dato\epicduel\github_bot\images\low_xButton'

# Get a list of all .png files
png_files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]

# Sort the files (optional, for consistency)
png_files.sort()

# Rename each file
for i, filename in enumerate(png_files, start=71):
    old_path = os.path.join(directory, filename)
    new_filename = f'xbutton{i}.png'
    new_path = os.path.join(directory, new_filename)
    os.rename(old_path, new_path)
    print(f'Renamed: {filename} -> {new_filename}')