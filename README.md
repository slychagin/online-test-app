# online-test-app
### Online test web application on Django


В качестве фронтэнда использован шаблон интернет-магазина на Bootstrap.
Бэкэнд реализован на Django Framework с использованием СУБД PostgreSQL.

Описание возможностей и функционала сайта:
- реальное eCommerce приложение написанное на Python и Django Framework;
- реализована кастомная модель пользователя (регистрация и логирование пользоввателей по email и паролю);
- регистрация с активацией через почту, логирование пользователей, сброс пароля, забыл пароль;
- создание товаров с описанием, ценами, фото и т.д. по категориям;
- карточка товара с описанием, фото, вариациями и галереей фото товара;
- корзина (в качестве идентификатора - ключ сессии), изменение количества товаров, удаление товаров;
- пагинация и поиск;
- реализована вариация товаров с возможностью добавления любого количества вариаций (цвет, размер и т.д.);
- группировка товаров в корзине по вариациям;
- заказы и функционал после заказа (страница благодарности, письмо на почту клиента и т.д.);
- подключена платежная система ЮKassa (тестовый режим);
- отзывы и оценка товаров;
- личный кабинет с возможностью просмотра заказов, изменение профиля, пароля;
- подключен telegram chatbot, который отправляет сообщение о новом заказе на указанный номер телефона;
- для удобства использования и администрирования сайта реализована админ панель со всеми необходимыми настройками.
#
### Интернет-магазин в работе:

#### *Общий вид сайта* :+1:
![Общий вид сайта](https://github.com/slychagin/mens-line-store/blob/master/demo_gifs/%D0%9E%D0%B1%D1%89%D0%B8%D0%B9%20%D0%B2%D0%B8%D0%B4.gif)
#

#### *Заказ и оценка товара*
![Заказ и оценка товара](https://github.com/slychagin/mens-line-store/blob/master/demo_gifs/%D0%97%D0%B0%D0%BA%D0%B0%D0%B7%20%D0%B8%20%D0%BE%D1%86%D0%B5%D0%BD%D0%BA%D0%B0%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0.gif)
#

#### *Личный кабинет*
![Личный кабинет](https://github.com/slychagin/mens-line-store/blob/master/demo_gifs/%D0%9B%D0%B8%D1%87%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%B0%D0%B1%D0%B8%D0%BD%D0%B5%D1%82.gif)
#

#### *Регистрация пользователя*
![Регистрация пользователя](https://github.com/slychagin/mens-line-store/blob/master/demo_gifs/%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F.gif)
#

#### *Админ панель (администрирование Django)*
![ЗАдмин панель](https://github.com/slychagin/mens-line-store/blob/master/demo_gifs/%D0%90%D0%B4%D0%BC%D0%B8%D0%BD%20%D0%BF%D0%B0%D0%BD%D0%B5%D0%BB%D1%8C.gif)
#

### Что использовано для создания сайта:
- Python 3, HTML, CSS, JavaScript, Bootstrap;
- Django Framework;
- PostgreSQL.

### Вы можете запустить этот проект локально просто сделав следующее:
- `git clone https://github.com/slychagin/mens-line-store.git`;
- у вас должен быть установлен Python;
- установите все зависимости из файла requirements.txt;
- также у вас должны быть все переменные окружения из файла .env-sample с 1 по 9 пункт;
- `python manage.py runserver`;
- для осуществления оплаты введите данные тестовой карты:
  - номер краты: 5555 5555 5555 4444;
  - срок действия: 01/30 (или любая будущая дата);
  - cvv код: 123 (или любой другой).