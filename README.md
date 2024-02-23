# online-test-app
### Online test web application on Django


В качестве фронтэнда использован шаблон Bootstrap.
Бэкэнд реализован на Django Framework.

Описание возможностей и функционала вэб приложения:
- реализована кастомная модель пользователя (регистрация и логирование пользоввателей по email и паролю);
- регистрация с активацией через почту, логирование пользователей, сброс пароля, забыл пароль;
- тесты могут проходить только зарегистрирванные пользователи;
- создание тестов с неограниченным количеством вопросов и ответов;
- тесты группируются по категориям;
- для удобства использования и администрирования сайта реализована админ панель со всеми необходимыми настройками;
- в админке можно создавать, удалять, редактировать категории, тесты, вопросы, ответы;
- можно устанавливать несколько правильных ответов, валидация, что хотябы один ответ должен быть правильным или неправильным;
- по завершении теста выдаются результаты с сохранением в базу данных по конкретному пользователю.
#
### Вэб приложение в работе:

#### *Общий вид приложения. Тестирование.* :+1:
![Общий вид приложения](https://github.com/slychagin/online-test-app/blob/master/demo/Testing.gif)
#

#### *Регистрация*
![Регистрация](https://github.com/slychagin/online-test-app/blob/master/demo/Register.gif)
#

#### *Админка*
![Админка](https://github.com/slychagin/online-test-app/blob/master/demo/admin.gif)
#

### Что использовано для создания сайта:
- Python 3, HTML, CSS, JavaScript, Bootstrap;
- Django Framework;
- SQLite.

### Вы можете запустить этот проект локально просто сделав следующее:
1. `git clone https://github.com/slychagin/online-test-app.git`
2. `python -m venv venv`
3. `venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. переименовать local_settings.example в local_settings.py и заполнить свои данные
6. `python manage.py makemigrations`
7. `python manage.py migrate`
8. `python manage.py runserver`

