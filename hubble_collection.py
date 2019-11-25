import requests
from pathlib import Path
from hubble import get_image_from_hubble


Path('images').mkdir(parents=True,exist_ok=True)
path = Path('images')
url = 'http://hubblesite.org/api/v3/images/spacecraft?page=all'
responses = requests.get(url,verify=False)
print(responses.json()[0]['id'])
for response in responses:
        image_id = response[0]
        print(image_id)
        get_image_from_hubble(image_id)
