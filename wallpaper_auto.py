import requests
import random
import os

from PIL import Image, ImageDraw, ImageFont

import ctypes



def set_wallpaper(image_path):
    # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def download_random_wallpaper(file_path):
    # Specify the number of images to select from (e.g., 10)
    num_images = 10
    rand_index = random.randint(0, num_images-1)
    
    print('rand_index',rand_index)

    # Fetching the Bing's daily image JSON
    url = f'https://www.bing.com/HPImageArchive.aspx?format=js&idx={rand_index}&n=1&mkt=en-US'
    response = requests.get(url)
    data = response.json()

    # Extracting the image URL
    image_url = data['images'][0]['url']
    full_image_url = 'https://www.bing.com' + image_url
    #print(full_image_url)
    title = data['images'][0]['title']
    # Downloading the image
    response = requests.get(full_image_url)
    image_data = response.content

    # Creating the "wallpaper" directory if it doesn't exist
    #os.makedirs("wallpaper", exist_ok=True)

    with open(file_path, 'wb') as file:
        file.write(image_data)

    #print(f'Wallpaper downloaded and saved as {file_path}!')
    
    return title

def add_text_to_image(photo_path, text):
    # 打开照片
    image = Image.open(photo_path)
    draw = ImageDraw.Draw(image)
    
    # 获取照片的宽度和高度
    image_width, image_height = image.size
    
    # 设置字体
    font_size = 120
    font = ImageFont.truetype('segoeui.ttf', font_size)
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (image_width - text_width) // 2
    if text_x < 0:
        font_size = 80
        font = ImageFont.truetype('segoeui.ttf', font_size)
        text_width, text_height = draw.textsize(text, font=font)
    
    # 计算字符串的位置
    text_x = (image_width - text_width) // 2
    text_y = (image_height - text_height) // 5
    
    # 绘制黑色描边
    border_size = 2
    border_color = 'black'
    draw.text((text_x - border_size, text_y), text, font=font, fill=border_color)
    draw.text((text_x + border_size, text_y), text, font=font, fill=border_color)
    draw.text((text_x, text_y - border_size), text, font=font, fill=border_color)
    draw.text((text_x, text_y + border_size), text, font=font, fill=border_color)
    
    # 绘制白色字体
    text_color = 'white'
    draw.text((text_x, text_y), text, font=font, fill=text_color)
    
    # 保存修改后的照片
    image.save(photo_path)

dir_path = os.path.dirname(os.path.realpath(__file__))
# Saving the image to a file
file_path = dir_path + "\\wallpaper\\1.jpg"
print('file_path',file_path)
# Calling the function to download a random wallpaper
title = download_random_wallpaper(file_path)
# 调用函数添加文字到照片
add_text_to_image(file_path, title)
# Call the function to set the wallpaper
set_wallpaper(file_path)
