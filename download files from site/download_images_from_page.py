import requests
from bs4 import BeautifulSoup
#gets page (HTML code from site), link - 'https://zastavok.net/', image_number - count
#download images, and return image number
def download_images_from_page(page: str, link: str, image_number: int):
    img_count = image_number
    soup = BeautifulSoup(page, 'lxml')
    block_photo = soup.find("div", class_="block-photo")
    image_containers = block_photo.find_all('div', class_="short_full")

    for image in image_containers:
        image_link = image.find('a').get('href')
        responce_image = requests.get(f'{link}{image_link}').text
        download_soup = BeautifulSoup(responce_image, 'lxml')
        download_link = download_soup.find('div', class_='image_data').find('div', class_='block_down').\
            find('a').get('href')
        result_link = f'{link}{download_link}'
        
        #download images  
        image_bytes = requests.get(result_link).content
        with open(f'./imgs/image_{img_count}.jpg', "wb") as file:
            file.write(image_bytes)    
        
        print(f"download image_{img_count} was successful")
        img_count += 1


    return img_count