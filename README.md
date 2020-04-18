# Загрузка фотографий в Instagram 

C помощью библиотеки ```instabot```, а также ```API``` : ```SpaceX``` и ```Hubble```,<br>
мы будем загружать фотографии космоса, а так же, запуск ракет Fulcon.

# How to install
Python3 have to be already installed. Then use pip (or pip3, there is a contravention with Python2) to install dependencies: :<br>

``` git clone https://github.com/djeck1432/instagram_bot.git ```

After you downloaded the repository open a folder ```instagram_bot``` using next command: <br>

```cd instagram_bot```

Now all of the required libraries and modules have to be installed:<br>

```pip install -r requirements.txt ```<br>

Now we are ready for the script .

# Как запустить 

Для начала, нам нужно скачать изображения: 

``` python hubble.py ``` 
``` python spacex.py ```
После, можем загружать их в ```Instagram``` , для этого, нужно подключиться к ```Instagram```.<br>
при запуске кода 

``` python main.py ```

```instabot``` запросить у вас ```INSTAGRAM_USER_NAME``` , а так же ```INSTAGRAM_PASSWORD```.

Готово, мы загрузили изображение с космосом и запуском ракет в ваш ```Instagram```. 

