#!/usr/bin/env python3
import requests
import random
import os
import platform
import subprocess
from PIL import Image, ImageDraw, ImageFont
import time
import shutil
import ctypes



def set_wallpaper(image_path):
    system = platform.system()

    if system == "Windows":
        # Set wallpaper on Windows
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

    elif system == "Darwin":
        abs_path = os.path.abspath(image_path)

        # Workaround: Copy image to a temporary location with a timestamped filename
        tmp_wallpaper_dir = os.path.expanduser("~/Library/Application Support/WallpaperCache")
        os.makedirs(tmp_wallpaper_dir, exist_ok=True)

        timestamped_image = os.path.join(tmp_wallpaper_dir, f"wallpaper_{int(time.time())}.jpg")
        shutil.copy(abs_path, timestamped_image)

        # Set the new file as wallpaper
        script = f'''
        tell application "System Events"
            set desktopCount to count of desktops
            repeat with desktopNumber from 1 to desktopCount
                tell desktop desktopNumber
                    set picture to "{timestamped_image}"
                end tell
            end repeat
        end tell
        '''
        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error setting wallpaper on macOS: {e}")

    else:
        print(f"Unsupported platform: {system}")

def download_random_wallpaper(file_path):
    try_connect = 100
    # Specify the number of images to select from (e.g., 10)
    num_images = 10
    rand_index = random.randint(0, num_images-1)
    
    print('rand_index',rand_index)

    # Fetching the Bing's daily image JSON
    url = f'https://www.bing.com/HPImageArchive.aspx?format=js&idx={rand_index}&n=1&mkt=en-US'
    i=0
    success = 0
    while (i<try_connect and success == 0):
        try:
            response = requests.get(url)
            data = response.json()
            success = 1
        except:
            i+=1
            print("err")
    # Extracting the image URL
    image_url = data['images'][0]['url']
    full_image_url = 'https://www.bing.com' + image_url
    #print(full_image_url)
    title = data['images'][0]['title']
    # Downloading the image
    
    i=0
    success = 0
    while (i<try_connect and success == 0):
        try:
            response = requests.get(full_image_url)
            success = 1
        except:
            i+=1
            print("err 2")

    image_data = response.content

    # Creating the "wallpaper" directory if it doesn't exist
    #os.makedirs("wallpaper", exist_ok=True)

    with open(file_path, 'wb') as file:
        file.write(image_data)

    #print(f'Wallpaper downloaded and saved as {file_path}!')
    
    return title

def add_text_to_image(photo_path, text):
    # Open the image
    image = Image.open(photo_path)
    draw = ImageDraw.Draw(image)

    # Get the width and height of the image
    image_width, image_height = image.size

    # Set the font
    font_size = 120
    font_path_primary = "/System/Library/Fonts/SFNS.ttf"
    font_path_fallback = "/System/Library/Fonts/Supplemental/Segoe UI.ttf"  # Or another valid fallback on your system

    font = ImageFont.truetype(font_path_primary, font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = (image_width - text_width) // 2
    if text_x < 0:
        # Adjust font size and switch font if text is too wide
        font_size = 80
        font = ImageFont.truetype(font_path_fallback, font_size)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

    # Calculate the position of the text
    text_x = (image_width - text_width) // 2
    text_y = (image_height - text_height) // 5

    # Draw black border (outline)
    border_size = 2
    border_color = 'black'
    draw.text((text_x - border_size, text_y), text, font=font, fill=border_color)
    draw.text((text_x + border_size, text_y), text, font=font, fill=border_color)
    draw.text((text_x, text_y - border_size), text, font=font, fill=border_color)
    draw.text((text_x, text_y + border_size), text, font=font, fill=border_color)

    # Draw white text on top
    text_color = 'white'
    draw.text((text_x, text_y), text, font=font, fill=text_color)

    # Save the modified image
    image.save(photo_path)

dir_path = os.path.dirname(os.path.realpath(__file__))
# Saving the image to a file
file_path = dir_path + "/1.jpg"
print('file_path',file_path)
# Calling the function to download a random wallpaper
title = download_random_wallpaper(file_path)
# 调用函数添加文字到照片
add_text_to_image(file_path, title)
# Call the function to set the wallpaper
set_wallpaper(file_path)
