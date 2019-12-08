import argparse

parser = argparse.ArgumentParser(description='Day 8 Part 1')
parser.add_argument('image_width', type=int, help='The width of the image')
parser.add_argument('image_height', type=int, help='The height of the image')
args = parser.parse_args()
final_image = []
for row in range(args.image_height):
    final_image.append([2]*args.image_width)

with open('input.txt','r') as file:
    image = [int(pixel) for pixel in file.readline().strip()]
pixels_per_layer = args.image_width * args.image_height
for layer in range(len(image)//pixels_per_layer):
    for pixel in range(pixels_per_layer):
        row = pixel//args.image_width
        col = pixel%args.image_width
        final_image[row][col] = final_image[row][col] if final_image[row][col] < 2 else (image[layer*pixels_per_layer+pixel] if image[layer*pixels_per_layer+pixel] < 2 else 2)

print('image')
for row in final_image:
    print("".join([str(col) if col == 1 else ' ' for col in row]))