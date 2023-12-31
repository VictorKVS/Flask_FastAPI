# Flask_FastAPI
Фреймворки Flask и FastAPI ( лекция - семинары)
# Flask-FastAPI

## 1.Introduction to Flask

### lesson_1/homework/task_8
Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.

### /lesson_1/homework/task_9
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.

## 2. Flask (continuation)

### /lesson_2/seminar/task_9.py
1) Создать страницу, на которой будет форма для ввода имени
и электронной почты
2) При отправке которой будет создан cookie файл с данными
пользователя
3) Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
4) На странице приветствия должна быть кнопка "Выйти"
5) При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.

## 3. Additional Flask features

### /lesson_3_SQLAlchemy/homework/task_2_library
1) Создать базу данных для хранения информации о книгах в библиотеке.
2) База данных должна содержать две таблицы: "Книги" и "Авторы".
3) В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
4) В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
5) Необходимо создать связь между таблицами "Книги" и "Авторы".
6) Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.

### /lesson_3_SQLAlchemy/homework/task_3_students/
1) Создать базу данных для хранения информации о студентах и их оценках в
учебном заведении.
2) База данных должна содержать две таблицы: "Студенты" и "Оценки".
3) В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
и email.
4) В таблице "Оценки" должны быть следующие поля: id, id студента, название
предмета и оценка.
5) Необходимо создать связь между таблицами "Студенты" и "Оценки".
6) Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их оценок.

### /lesson_3_SQLAlchemy/homework/task_4_wtform
1)Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
содержать следующие поля:
    ○ Имя пользователя (обязательное поле)
    ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
    ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
    ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
2) После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
заполнено или данные не прошли валидацию, то должно выводиться соответствующее
сообщение об ошибке.
3) Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
об ошибке.

### /lesson_3_SQLAlchemy/homework/task_5_wtform2
1) Создать форму регистрации для пользователя.
2) Форма должна содержать поля: имя, электронная почта,
пароль (с подтверждением), дата рождения, согласие на
обработку персональных данных.
3) Валидация должна проверять, что все поля заполнены
корректно (например, дата рождения должна быть в
формате дд.мм.гггг).
4) При успешной регистрации пользователь должен быть
перенаправлен на страницу подтверждения регистрации.

## 4. Multitasking (multiprocessing, threading, async)

### /lesson_4_Threading_Async/homework/task_7
1) Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
2) Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
3) Массив должен быть заполнен случайными целыми числами
от 1 до 100.
4) При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
5) В каждом решении нужно вывести время выполнения вычислений.

### /lesson_4_Threading_Async/homework/task_8
1) Напишите программу, которая будет скачивать страницы из
списка URL-адресов и сохранять их в отдельные файлы на
диске.
2) В списке может быть несколько сотен URL-адресов.
3) При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
4) Представьте три варианта решения.

### /lesson_4_Threading_Async/homework/task_9
1) Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
2) Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
3) Программа должна использовать многопоточный, многопроцессорный и
асинхронный подходы.
4) Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
5) Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы.

## 5. Introduction to FastAPI

### /lesson_5_FastAPI/seminar/main7
Создать RESTful API для управления списком задач. Приложение должно
использовать FastAPI и поддерживать следующие функции:

○ Получение списка всех задач.

○ Получение информации о задаче по её ID.

○ Добавление новой задачи.

○ Обновление информации о задаче по её ID.

○ Удаление задачи по её ID.

Каждая задача должна содержать следующие поля: 
ID (целое число),

Название (строка), 

Описание (строка), 

Статус (строка): todo, in progress, done.

Создайте модуль приложения и настройте сервер и маршрутизацию.

Создайте класс Task с полями id, title, description и status.

Создайте список tasks для хранения задач.

Создайте функцию get_tasks для получения списка всех задач (метод GET).

Создайте функцию get_task для получения информации о задаче по её ID
(метод GET).

Создайте функцию create_task для добавления новой задачи (метод POST).

Создайте функцию update_task для обновления информации о задаче по её ID
(метод PUT).

Создайте функцию delete_task для удаления задачи по её ID (метод DELETE).

## 6. Additional FastAPI features

### /lesson_6_More_FastAPI/seminar/main1.py
Разработать API для управления списком пользователей с
использованием базы данных SQLite. Для этого создайте
модель User со следующими полями:

○ id: int (идентификатор пользователя, генерируется автоматически)

○ username: str (имя пользователя)

○ email: str (электронная почта пользователя)

○ password: str (пароль пользователя)

API должно поддерживать следующие операции:

○ Получение списка всех пользователей: GET /users/
    
○ Получение информации о конкретном пользователе: GET /users/{user_id}/
    
○ Создание нового пользователя: POST /users/
    
○ Обновление информации о пользователе: PUT /users/{user_id}/
    
○ Удаление пользователя: DELETE /users/{user_id}/
    
Для валидации данных используйте параметры Field модели User.

Для работы с базой данных используйте SQLAlchemy и модуль databases.

### /lesson_6_More_FastAPI/seminar/main2.py
Создать веб-приложение на FastAPI, которое будет предоставлять API для
работы с базой данных пользователей. Пользователь должен иметь
следующие поля:

○ ID (автоматически генерируется при создании пользователя)
    
○ Имя (строка, не менее 2 символов)
    
○ Фамилия (строка, не менее 2 символов)
    
○ Дата рождения (строка в формате "YYYY-MM-DD")
    
○ Email (строка, валидный email)
    
○ Адрес (строка, не менее 5 символов)

API должен поддерживать следующие операции:

○ Добавление пользователя в базу данных
    
○ Получение списка всех пользователей в базе данных
    
○ Получение пользователя по ID
    
○ Обновление пользователя по ID
    
○ Удаление пользователя по ID
    
Приложение должно использовать базу данных SQLite3 для хранения пользователей.

### /lesson_6_More_FastAPI/seminar/main3.py
1) Создать API для управления списком задач.
2) Каждая задача должна содержать поля "название",
"описание" и "статус" (выполнена/не выполнена).
3) API должен позволять выполнять CRUD операции с
задачами.

### /lesson_6_More_FastAPI/seminar/main4.py
Напишите API для управления списком задач. Для этого создайте модель Task
со следующими полями:

○ id: int (первичный ключ)
    
○ title: str (название задачи)
    
○ description: str (описание задачи)
    
○ done: bool (статус выполнения задачи)

API должно поддерживать следующие операции:

○ Получение списка всех задач: GET /tasks/
    
○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
    
○ Создание новой задачи: POST /tasks/
    
○ Обновление информации о задаче: PUT /tasks/{task_id}/
    
○ Удаление задачи: DELETE /tasks/{task_id}/
    
Для валидации данных используйте параметры Field модели Task.

Для работы с базой данных используйте SQLAlchemy и модуль databases.

### /lesson_6_More_FastAPI/seminar/main6.py
Необходимо создать базу данных для интернет-магазина. 

База данных должна состоять из трех таблиц: товары, заказы и пользователи. 

Таблица товары должна содержать информацию о доступных товарах, их описаниях и ценах. 

Таблица пользователи должна содержать информацию о зарегистрированных пользователях 
магазина. 

Таблица заказы должна содержать информацию о заказах, сделанных пользователями.

○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
имя, фамилия, адрес электронной почты и пароль.

○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
название, описание и цена.

○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
заказа.

Создайте модели pydantic для получения новых данных и
возврата существующих в БД для каждой из трёх таблиц
(итого шесть моделей).

Реализуйте CRUD операции для каждой из таблиц через
создание маршрутов, REST API (итого 15 маршрутов).

○ Чтение всех

○ Чтение одного

○ Запись

○ Изменение

○ Удаление
