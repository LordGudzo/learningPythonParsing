import requests
from download_images_from_page import download_images_from_page 

page_number = 1
image_number = 1
link = 'https://zastavok.net/'

for i in range(2):
    responce_page = requests.get(f"{link}{page_number}").text
    image_number = download_images_from_page(responce_page, link, image_number)
    print(f'\n!!!!!image numer: {image_number}!!!!!!')
    page_number += 1