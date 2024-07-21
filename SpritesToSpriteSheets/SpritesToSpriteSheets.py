from PIL import Image
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import argparse

def create_spritesheet(image_paths, sprite_width, sprite_height, output_path):
    # Determine the number of sprites and calculate the dimensions of the spritesheet
    num_sprites = len(image_paths)
    sprites_per_row = min(10, num_sprites)
    num_rows = (num_sprites + sprites_per_row - 1) // sprites_per_row
    sheet_width = sprite_width * sprites_per_row
    sheet_height = sprite_height * num_rows

    # Create a new blank image with a transparent background
    spritesheet = Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))

    # Load each sprite and paste it into the spritesheet
    for i, image_path in enumerate(image_paths):
        sprite = Image.open(image_path).convert("RGBA")
        if sprite.size != (sprite_width, sprite_height):
            sprite = sprite.resize((sprite_width, sprite_height), Image.ANTIALIAS)
        x = (i % sprites_per_row) * sprite_width
        y = (i // sprites_per_row) * sprite_height
        spritesheet.paste(sprite, (x, y))

    # Save the final spritesheet
    spritesheet.save(output_path)

def select_images():
    Tk().withdraw()  # Prevent the root window from appearing
    file_paths = askopenfilenames(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    return file_paths

# Main execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a spritesheet from selected images.")
    parser.add_argument('--output', required=True, help='Output file name for the spritesheet.')
    args = parser.parse_args()
    image_paths = select_images()
    if image_paths:
        sprite_width = 64  # Example sprite width
        sprite_height = 64  # Example sprite height
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, 'outputs')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, args.output)
        create_spritesheet(image_paths, sprite_width, sprite_height, output_path)
        print(f"Spritesheet saved to {output_path}")
    else:
        print("No images selected.")