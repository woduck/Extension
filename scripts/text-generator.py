import math
import gradio as gr
from PIL import Image, ImageDraw, ImageOps, ImageFont
from modules import processing, shared, images, devices, scripts
from modules.processing import StableDiffusionProcessing
from modules.processing import Processed
from modules.shared import opts, state

class TextGener():
    def __init__(self, input_text, font_size, num_layers, offset):
        self.input_text = input_text
        self.font_size = font_size
        self.num_layers = num_layers
        self.offset = offset
        
    def create_text(self):
        font = ImageFont.truetype("arialbd.ttf", self.font_size)
        # font = ImageFont.load_default(self.font_size)
        # Create a new image with a white background
        image = Image.new("RGB", (512, 512), (255, 255, 255))

        # Get the size of the text and calculate its position in the center of the image
        text_size = font.getbbox(self.input_text)
        text_x = (image.width - text_size[2]) / 2
        text_y = (image.height - text_size[3]) / 2

        # A method to create thicker text on the image
        # Define the number of shadow layers to create and the offset distance
        

        # Draw the text onto the image multiple times with a slight offset to create a shadow effect
        draw = ImageDraw.Draw(image)
        for i in range(self.num_layers):
            x = text_x + (i * self.offset)
            y = text_y + (i * self.offset)
            draw.text((x, y), self.input_text, font=font, fill=(0, 0, 0))

        stroke_color = (0,0,0)

        # Draw the final text layer on top of the shadows
        draw.text((text_x, text_y), self.input_text, font=font, fill=(255, 255, 255), stroke_width=1, stroke_fill=stroke_color)

        return image
        
class Script(scripts.Script):
    def title(self):
        return "Text generator"

    def show(self, is_img2img):
        return is_img2img

    def ui(self, is_img2img):
        with gr.Row():
            input_text = gr.Textbox(label="Text Input", lines=3)
            font_size = gr.Slider(label='Font Size', minimum=10, maximum=150, step=20, value=100, visible=True, interactive=True)
            num_layers = gr.Slider(label='Num Layers', minimum=2, maximum=15, step=1, value=8, visible=True, interactive=True)
            offset = gr.Slider(label='Offset', minimum=2, maximum=5, step=1, value=2, visible=True, interactive=True)
            return input_text, font_size, num_layers, offset

    def run(self, p, input_text, font_size, num_layers, offset):
        text = TextGener(input_text, font_size, num_layers, offset)
        image = text.create_text()
        
        return Processed(p, image)