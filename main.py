import glob
from PIL import Image
import requests

def download_images(urls):
    cont = 1
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{cont}.png', 'wb') as file:
                file.write(response.content)
            cont+=1


def stitch(file_extension):
    files = sorted(glob.glob(f'*.{file_extension}'))
    images = [Image.open(file) for file in files]
    background_width = max([image.width for image in images])
    background_height = sum([image.height for image in images])
    background = Image.new('RGBA', (background_width, background_height), (255, 255, 255, 255))
    y = 0
    for image in images:
        background.paste(image, (0, y))
        y += image.height
    background.save('joined_image.png')


urls = open("urls.txt").read().splitlines()
download_images(urls)
stitch('png')

