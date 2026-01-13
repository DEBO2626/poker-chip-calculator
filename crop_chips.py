"""
Crop all4chips.png into individual poker chip images
"""
from PIL import Image
import os

# Input and output paths
input_image = r"c:\Users\john_\Desktop\poker-chip-web\frontend\assets\all4chips.png"
output_dir = r"c:\Users\john_\Desktop\poker-chip-web\frontend\assets"

# Load the image
img = Image.open(input_image)
width, height = img.size

print(f"Image size: {width}x{height}")

# Calculate chip positions (2x2 grid)
chip_width = width // 2
chip_height = height // 2

# Define crop regions and output filenames
chips = [
    {
        'name': 'chip-5-red.png',
        'box': (0, 0, chip_width, chip_height),  # Top-left (Red $5)
        'label': 'Red $5'
    },
    {
        'name': 'chip-25-green.png',
        'box': (chip_width, 0, width, chip_height),  # Top-right (Green $25)
        'label': 'Green $25'
    },
    {
        'name': 'chip-100-black.png',
        'box': (0, chip_height, chip_width, height),  # Bottom-left (Black $100)
        'label': 'Black $100'
    },
    {
        'name': 'chip-500-purple.png',
        'box': (chip_width, chip_height, width, height),  # Bottom-right (Purple $500)
        'label': 'Purple $500'
    }
]

# Crop and save each chip
for chip in chips:
    cropped = img.crop(chip['box'])
    output_path = os.path.join(output_dir, chip['name'])
    cropped.save(output_path, 'PNG')
    print(f"[OK] Saved {chip['label']}: {chip['name']} ({cropped.size[0]}x{cropped.size[1]})")

print(f"\n[SUCCESS] All chips cropped successfully!")
print(f"Output folder: {output_dir}")
