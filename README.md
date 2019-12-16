# Загрузка фотографий в Instagram 

C помощью библиотеки ```instabot```, а также ```API``` : ```SpaceX``` и ```Hubble```,<br>
мы будем загружать фотографии космоса, а так же, запуск ракет Fulcon.

# Как установить 

1)Откроем терминал(MacOs) или консоль(Linux) и с помощью терминала, установим репозиторий на наш компютер:

``` git clone https://github.com/djeck1432/instagram_bot.git```

2)Откроем установленый репозиторий : 

```cd instagram_bot```

3)Теперь, запустив виртуальное окружение, да бы избежать конфликта версий библиотек которые использует код с теми, которые уже у вас установлены:

````source env/bin/activate ````

4)После этого, осталось устнановить все необходимые библиотеки:

```pip install -r requirements.txt ```

# Как запустить 

Для начала, нам нужно скачать изображения: 

``` python hubble.py ``` 
``` python spacex.py ```
После, можем загружать их в ```Instagram``` , для этого, нужно подключиться к ```Instagram```.<br>
при запуске кода 

``` python main.py ```

```instabot``` запросить у вас ```INSTAGRAM_USER_NAME``` , а так же ```INSTAGRAM_PASSWORD```.

Готово, мы загрузили изображение с космосом и запуском ракет в ваш ```Instagram```. 
