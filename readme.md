python -m venv /path/to/new/virtual/environment
pip install django
django-admin startproject mysite
python manage.py startapp myapp

pip freeze > requirements.txt  
pip install -r requirements.txt
python manage.py createsuperuser

from myapp.models import *

pip install djangorestframework

https://github.com/PonomaryovVladyslav/PythonCources/blob/master/lesson37.md

_________________________________________________________________
Все варианты подразумевают, логин, логаут, регистрацию.

Во всех вариантах, обычный пользователь, не админ должен быть автоматически разлогинен через 1 минуту после последнего 
действия попавшего на сервер (Через рест должен умирать токен)!

На все действия любого из вариантов нужно реализовать REST API тоже (в любой момент я могу сказать, а следующее действие
выполняем через постман, и наоборот, а теперь зайди на сайт и продолжай действие)!

Роли - пользователь, админ
_____________________________________________________________________
Вариант 1)

Сайт кинотеатра.

Действия:

Админ:

Может создавать зал кинотеатра, в котором он должен указать имя зала, размер зала

Может создавать сеансы, у которых указывается время начала, время окончания, и даты показа (с 5 февраля по 15 февраля 
2021 года, например), цену билета на сеанс.

Может изменять зал или сеанс, если не было куплено ни одного билета в этот зал или в на этот сеанс.

Сеансы в одном зале не могут накладываться друг на друга.

Пользователь: 

Может просмотреть список сеансов на сегодня и в отдельной вкладке на завтра, кол-во свободных мест в зале, купить 
билет\билеты на сеанс, если в зале закончились места, должен получить соответствующее уведомление.

Может просмотреть список совершенных им покупок, и общую затраченную сумму за всё время.

Сеансы можно сортировать по цене или времени начала.

Не залогиненный пользователь, видит список, может его отсортировать, не может ничего купить

По ресту, добавить возможность получения информации о всех сеансах на сегодня, которые начинаются в определённый 
промежуток времени и\или идут в конкретном зале.
