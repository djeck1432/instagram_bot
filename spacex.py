import requests
from pathlib import Path

Path('images').mkdir(parents = True , exist_ok = True)
path = Path('images')
url = 'https://api.spacexdata.com/v3/launches/latest?pretty=true'
response = requests.get(url)
response.raise_for_status()
spacex_image_links = response.json()['links']['flickr_images']
Path('images').mkdir(parents = True , exist_ok = True)
path = Path('images')
def fetch_spacex_last_launch():
  for image_number,image in enumerate(spacex_image_links):
    filename = 'spacex'+ str(image_number+1)+'.jpg'
    response = requests.get(image)
    response.raise_for_status()
    with open(path/filename,mode='wb') as image:
      image.write(response.content)

fetch_spacex_last_launch()
