from PIL import Image, ImageDraw
from collections import Counter

def get_common_colors(image_path, num_colors=2):
    original_image = Image.open(image_path)
    rgb_image = original_image.convert("RGB")
    pixel_colors = list(rgb_image.getdata())
    color_counter = Counter(pixel_colors)
    common_colors = color_counter.most_common(num_colors)
    return [color[0] for color in common_colors]

def create_color_gradient(color1, color2, image_size=(500, 500)):
    gradient_image = Image.new("RGB", image_size)
    draw = ImageDraw.Draw(gradient_image)
    
    for y in range(image_size[1]):
        r = int(color1[0] * (1 - y / image_size[1]) + color2[0] * (y / image_size[1]))
        g = int(color1[1] * (1 - y / image_size[1]) + color2[1] * (y / image_size[1]))
        b = int(color1[2] * (1 - y / image_size[1]) + color2[2] * (y / image_size[1]))
        draw.line([(0, y), (image_size[0], y)], fill=(r, g, b))
    
    return gradient_image

if __name__ == "__main__":
    original_image_path = "1.jpg"
    output_image_path = "gradient_image.jpg"
    
    common_colors = get_common_colors(original_image_path, num_colors=2)
    gradient_image = create_color_gradient(common_colors[0], common_colors[1])
    gradient_image.save(output_image_path)
    
    print("Gradient image created successfully!")

