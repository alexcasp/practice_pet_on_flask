Практический проект на Flask

Домашнее задание
Техническое задание: Сервис для работы с Календарем.

Требования:

— API интерфейс CRUD — Добавление / Список / Чтение / Обновление / Удаление
— модель данных "Событие": ID, Дата, Заголовок, Текст
— локальное хранилище данных
— максимальная длина заголовка — 30 символов
— максимальная длина поля Текст — 200 символов
— нельзя добавить больше одного события в день
— API интерфейс: /api/v1/calendar/… (по аналогии с заметкой)
— формат данных: "ГГГГ-ММ-ДД|заголовок|текст" (по аналогии с заметкой)

Написать и протестировать приложение, по аналогии с сервисом заметок из Воркшопа.

/======================Требования==================================/

- Python 3.8+
- Flask (`pip install flask`)

/======================Инструкция по запуску==================================/

Установить зависимости

    pip install -r requirements.txt

Запустите приложение

    python app.py


/======================Тестирование API==================================/
1. Создать событие:

    curl -X POST -d "2025-04-01|Встреча|Синхронизация" http://localhost:5000/api/v1/calendar/

2. Получить список всех событий:

    curl http://localhost:5000/api/v1/calendar/

3. Прочитать конкретное событие:

    curl http://localhost:5000/api/v1/calendar/1/ 

4. Обновить событие:

    curl -X PUT -d "2025-04-01|Обновленная встреча|Синхронизация" http://localhost:5000/api/v1/calendar/1/

5. Удалить событие:

    curl -X DELETE http://localhost:5000/api/v1/calendar/1/

Тестовые случаи

1. Попробовать создать два события на одну дату (должно завершиться ошибкой)

    curl -X POST -d "2025-04-01|Встреча1|Текст1" http://localhost:5000/api/v1/calendar/
    curl -X POST -d "2025-04-01|Встреча2|Текст2" http://localhost:5000/api/v1/calendar/

2. Попробовать создать событие с длинным заголовком (>30 символов)

    curl -X POST -d "2025-04-02|Этот заголовок слишком длинный|Текст" http://localhost:5000/api/v1/calendar/

3. Попробовать создать событие с длинным текстом (>200 символов)

    curl -X POST -d "2025-04-02|Встреча|Этот текст слишком длинный, чтобы быть действительным, потому что он превышает 200 символов, что является максимальной допустимой длиной для текстового поля в нашей реализации сервиса календаря и должен вызвать ошибку валидации" http://localhost:5000/api/v1/calendar/
