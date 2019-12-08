import argparse

parser = argparse.ArgumentParser(description='Day 8 Part 1')
parser.add_argument('image_width', type=int, help='The width of the image')
parser.add_argument('image_height', type=int, help='The height of the image')
parser.add_argument('pixel_value_1', type=int, help='The first pixel value count on zero layer to count')
parser.add_argument('pixel_value_2', type=int, help='The second pixel value count on zero layer to count')
args = parser.parse_args()

with open('input.txt','r') as file:
    image = [int(pixel) for pixel in file.readline().strip()]
pixels_per_layer = args.image_width * args.image_height
zero_layer = 0
zero_layer_count = sum([1 if pixel == 0 else 0 for pixel in image[0:pixels_per_layer]])
print(zero_layer, zero_layer_count)
for layer in range(len(image)//pixels_per_layer):
    zero_count = sum([1 if pixel == 0 else 0 for pixel in image[layer*pixels_per_layer:(layer+1)*pixels_per_layer]])
    if zero_count < zero_layer_count:
        zero_layer = layer
        zero_layer_count = zero_count
print(zero_layer, zero_layer_count)
p1_value = sum([1 if pixel == args.pixel_value_1 else 0 for pixel in image[zero_layer*pixels_per_layer:(zero_layer+1)*pixels_per_layer]])
p2_value = sum([1 if pixel == args.pixel_value_2 else 0 for pixel in image[zero_layer*pixels_per_layer:(zero_layer+1)*pixels_per_layer]])
print(p1_value, p2_value, p1_value*p2_value)