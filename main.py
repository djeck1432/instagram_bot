from os import listdir
from os.path import isfile
from os.path import join as joinpath
from PIL import Image
from instabot import Bot
from dotenv import load_dotenv
import os


path = './images'
name_of_images = []
for name_of_image  in listdir(path):
  if isfile(joinpath(path,name_of_image)):
    name_of_images.append(name_of_image)

def get_croping_image(image):
    path_to_image = os.path.join(path,image)
    image = Image.open(path_to_image)
    name_and_format = (path_to_image.split('/'))[-1]
    if image.width > image.height:
      coordinates = (image.width - image.height,0, image.width, image.height)
    else:
      coordinates = (0,image.height - image.width, image.width, image.height)
    return (image.crop(coordinates)).save(os.path.join(path,'new_'+name_and_format))

def make_square_image():
    for image in name_of_images:
        print(image)
        get_croping_image(image)
        os.remove(os.path.join(path, image))


if __name__ == '__main__':
  load_dotenv()
  secret_username = os.getenv('INSTAGRAM_USER_NAME')
  secret_password = os.getenv('INSTAGRAM_PASSWORD')
  bot = Bot()
  bot.login(username=secret_username, password=secret_password)
  make_square_image()
  for image in name_of_images:

      bot.upload_photo(image ,caption= 'it is first photo')
      print(bot.api.last_response)
