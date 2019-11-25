from os import listdir
from os.path import isfile
from os.path import join as joinpath
from PIL import Image
from instabot import Bot
from dotenv import load_dotenv
import os
import glob


path = './images'
name_of_images = []
for name_of_image  in listdir(path):
  if isfile(joinpath(path,name_of_image)):
    name_of_images.append(name_of_image)

def croping_image(image):
    path_to_image = os.path.join(path,image)
    image = Image.open(path_to_image)
    # x = image.width/image.height
    # coordinates = (image.width/x,0,image.width,image.height)
    # cropped = image.crop(coordinates)
    # return cropped.show()



# image = Image.open('32.jpg')
# coordinates = (image.width - 1080,image.height-1080,image.width,image.height)
# cropped = image.crop(coordinates)
# cropped.save('new_32.jpg')
# download_image(url,filename)
#
if __name__ == '__main__':
  load_dotenv()
  secret_username = os.getenv('INSTAGRAM_USER_NAME')
  secret_password = os.getenv('INSTAGRAM_PASSWORD')
  bot = Bot()
  bot.login(username=secret_username, password=secret_password)
  bot.upload_photo(os.path.join(path,name_of_images[2]),caption= 'it is first photo')
  print(bot.api.last_response)