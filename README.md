### WEB Сервис

**Стек технологий:**

    1. Python 3.10
    2. Django 4.0
    3. PostgreeSQL
    4. Docker


**Установка проекта на сервере**

    - Копируем репозиторий
    - Устанавливаем docker
    - Устанавливаем docker-compose

    - Находясь в дирректории, где лежит docker-compose.yml выполнить команду:
          - sudo docker-compose build
          - Проект достаточно долго собирается, из-за того, что pandas собирается из исходников.

    - После того, как проект соберется, необходимо запустить контейнеры:
          - sudo docker-compose up -d

    - Далее необходимо выполнить миграции
          - sudo docker-compose exec web python manage.py flush --no-input
          - sudo docker-compose exec web python manage.py migrate

    - Coздадим суперпользователя для проекта
          - sudo docker-compose exec web python manage.py createsuperuser
          - далее в предлагаемых полях введите необходимые данные, например
                - Логин: admin (Enter)
                - E-mail: можно оставить пустым (Enter)
                - Пароль: ***  (Enter)
                - Пароль еще раз: ***  (Enter)
    
    - Теперь можем при необходимости перейти на страницу проекта:
          - 127.0.0.1:8051
    
    - Зайти в админку проекта, используя введенные ранее данные администратора:
          - 127.0.0.1:8051/admin

    - Или сразу же воспользоваться API


**Объект VPS**

    - uid - идентификатор
    - cpu - количество ядер
    - ram - объем RAM
    - hdd - объем HDD
    - status - статус сервера (started, blocked, stopped)


**API поддерживает операции**

    - (POST) создать VPS.

        - 127.0.0.1:8051/methodapi
        - BODY JSON, например:
        {
            "data":{
                "cpu":6,
                "ram":256,
                "hdd":1,
                "status":0
            }
        }

    - (GET) получить VPS по uid. Принимает одно или несколько значений uid через ",":

        - 127.0.0.1:8051/methodapi?uid=17d13f5f-29ca-468e-a1ac-8e23cfb9ded7
        - 127.0.0.1:8051/methodapi?uid=17d13f5f-29ca-468e-a1ac-8e23cfb9ded7,880a0d6c-c325-4831-8064-d8649756b44c

    - (GET) получить список VPS с возможностью фильтрации по параметрам

        - 127.0.0.1:8051/methodapi?cpu=...&ram=...&hdd=...&status=...

    - (PUT) перевести VPS в другой статус
    
        - 127.0.0.1:8051/methodapi
        - Параметры, например:
          "uid":17d13f5f-29ca-468e-a1ac-8e23cfb9ded7,
          "status":2,
