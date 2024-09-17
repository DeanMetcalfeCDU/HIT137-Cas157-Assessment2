# https://github.com/DeanMetcalfeCDU/HIT137-Cas157-Assessment2
# Created by Adrian Voljak

#Chapter 1
#Libraries Needed for both the algorithm and the image modifier
import time
from PIL import Image

#Algorithm to Generate Random Number
current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(generated_number)

#Image Modifier
original_image_path = 'C:/Users/User/OneDrive/Desktop/University/Semester 2 2024/HIT137/HIT137 Group Assignment 2 - CAS157/chapter1.jpg'

chapter1 = Image.open(original_image_path)

pixels = chapter1.load()

width, height, = chapter1.size

red_pixel_sum = 0

for y in range(height):
    for x in range (width):
        r, g, b = pixels [x,y]
        updated_r = min(r + generated_number, 255)
        updated_g = min(g + generated_number, 255)
        updated_b = min(b + generated_number, 255)
        pixels[x, y] = (updated_r, updated_b, updated_g)

        red_pixel_sum += updated_r

chapter1out= 'chapter1out.png'
chapter1.save(chapter1out)

print(f"Sum of all red pixels is {red_pixel_sum}")
