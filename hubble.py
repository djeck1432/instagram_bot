import requests
from pathlib import Path

Path('images').mkdir(parents=True,exist_ok=True)
path = Path('images')

def get_picture_format(image_url):
  split_url = image_url.split('.')
  return split_url[-1]

def get_image_from_hubble(image_id):
  url = 'http://hubblesite.org/api/v3/image/' + str(image_id)
  response = requests.get(url,verify=False)
  image_files = response.json()['image_files']
  file_url = 'https:'+ image_files[-1]['file_url']
  print(file_url)
  image_download = requests.get(file_url,verify=False)
  print(image_download.raise_for_status())
  filename = str(image_id) + '.' + get_picture_format(file_url)
  with open(path/filename,mode='wb') as filename:
    filename.write(image_download.content)


get_image_from_hubble('3811')
