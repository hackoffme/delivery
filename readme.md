# DeliveryApp
Готовый бот для доставки с админкой на django. 

## Инструкция по развертыванию 
Предполагается что у вас уже есть сервер с настроенным docker и доменным именем (можно второго уровня, имя необходимо certbot для генерации сертификата).

Создайте два бота с помощью @BotFather, сохраните токены
Первый бот будет использоваться для заказов, второй бот будет в группе писать сообщения для администратора.
Второго бота необходимо добавить в группу телеграм, и узнать ID этой группы с помощью бота @myidbot (добавив его в группу и выполнив команду /getgroupid). Сохраните этот id.

Загрузисте проект
```
git clone https://github.com/hackoffme/delivery.git
```
Затем зайдите в папку ./env_file и уберите из имени всех файлов _EXAMPLE. Заполните все файлы в соответствии с коментариями в них.
Аналогично сделайте с файлом ./.env_EXAMPLE

Выполните `docker-compose -f ./docker-compose-initial.yml up --build`
Эта команда запустит nginx с настройками `./nginx/initial/default.conf` и certbot для первичной генерации сертификата. Сертификат сохранится в хранилище docker. Эта необходимо только при первом запуске. 
В случае успеха увидите в консоли вывод 
```
delivery_admin-certbot-1  | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
delivery_admin-certbot-1  | If you like Certbot, please consider supporting our work by:
delivery_admin-certbot-1  |  * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
delivery_admin-certbot-1  |  * Donating to EFF:                    https://eff.org/donate-le
delivery_admin-certbot-1  | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
delivery_admin-certbot-1 exited with code 0
```

Выполните команду `docker-compose -f ./docker-compose-initial.yml down`, чтобы остановить ngxing

Если выполните `docker container  ls` в терминале, то должны увидеть
```
DRIVER    VOLUME NAME
local     843c8ae43513b74ce7976f45234a2174cfe65b8a7e44acff5f02a9635935150f
local     delivery_admin_certbot_conf
local     delivery_admin_certbot_www
```

Выполните команду `docker-compose up -- build django`.
После запуска django из свободной консоли полдключимся с админке с помощью команды `docker-compose exec django bash`.
Здесь нам надо будет применить миграции, создать суперпользователя, и если надо загрузить тестовые данные.
```
#Для миграции
pythom manage.py migrate

#Для создания суперпользоателя(логин и пароль как в 
#./env_file/.bot.env для пользователя api)
python manage.py createsuperuser
```
Собираем статические файлы
```
python manage.py collectstatic
```
Код ниже нужен для загрузки тестовых данных в админку. Чтобы можно было оценить работу приложения

```
#Загружаем в бд тестовые данные
python manage.py load
#Делаем ссылку на фото
cp -r  ./media/old /var/www/media
```

Закрываем консоль контейнера и завершаем работу django командой `docker-compose down`

После завершения работы запускаем приложение командой `docker-compose up --build -d`

Приложение готово к работе. 
Админка доступна по адресу вашего домена, по https.
Для заказа в боте нажмите start или напишите команду `/start`.
Выполните тестовый заказ, сообщение с заказом придет в группу ранее созданную группу. В админке также появится заказ. Приятного пользования :)
