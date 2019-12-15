import requests
import os
from pathlib import Path

Path('images').mkdir(parents=True, exist_ok=True)
PATH  = Path('images')

def get_picture_format(image_url):
  split_url = os.path.splitext(image_url)
  return split_url[-1]

def get_image_from_hubble(image_id):
  url = '{url}{image_id}'.format(url='http://hubblesite.org/api/v3/image/',image_id=str(image_id))
  response = requests.get(url,verify=False)
  image_files = response.json()['image_files']
  file_url = 'https:{}'.format(image_files[-1]['file_url'])
  image_download = requests.get(file_url,verify=False)
  image_download.raise_for_status()
  filename = '{number}{format}'.format(number=str(image_id),format=os.path.splitext(file_url)[-1])
  with open(PATH/filename,mode='wb') as filename:
    filename.write(image_download.content)


def main ():
  url = 'http://hubblesite.org/api/v3/images/spacecraft'
  params = {
    'page': 'all',
  }
  responses = requests.get(url, params=params, verify=False)
  for response in responses:
    image_id = response[0]
    get_image_from_hubble(image_id)


if __name__ == "__main__":
  main()

