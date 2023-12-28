import os
import math
import gradio as gr
from PIL import Image, ImageDraw, ImageOps, ImageFont


    
def create_text(input_text, font_size, num_layers, offset):
    # file_path = "./Text-generator/arial/arial.ttf"
    font = ImageFont.truetype("./arial_bold.ttf", font_size)
    # font = ImageFont.load_default(self.font_size)
    # Create a new image with a white background
    image = Image.new("RGB", (512, 512), (255, 255, 255))

    # Get the size of the text and calculate its position in the center of the image
    text_size = font.getbbox(input_text)
    text_x = (image.width - text_size[2]) / 2
    text_y = (image.height - text_size[3]) / 2

    # A method to create thicker text on the image
    # Define the number of shadow layers to create and the offset distance
    

    # Draw the text onto the image multiple times with a slight offset to create a shadow effect
    draw = ImageDraw.Draw(image)
    for i in range(num_layers):
        x = text_x + (i * offset)
        y = text_y + (i * offset)
        draw.text((x, y), input_text, font=font, fill=(0, 0, 0))

    stroke_color = (0,0,0)

    # Draw the final text layer on top of the shadows
    draw.text((text_x, text_y), input_text, font=font, fill=(255, 255, 255), stroke_width=1, stroke_fill=stroke_color)

    return image
def main():
    letters = create_text("HELLO", 150, 8 , 2)
    letters.show()
    
if __name__ == '__main__':
    main()