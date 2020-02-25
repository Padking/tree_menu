# tree_menu
Приложение "tree_menu"

## Описание

В данном репозитории находится приложение, позволяющее создавать древовидное меню. 
Написано с использованием фреймворка [Django](https://github.com/django/django).

### Особенности:

* реализовано с использованием пользовательского тега
* позволяет отображать несколько меню на одной html-странице

### Использование и его результат

  Создать меню в приложении Django-admin:
  ![f](https://github.com/Padking/tree_menu/blob/master/screenshots/)


  Создать заголовок 0-го уровня (корень меню):
  ![s]()
  
  Создать заголовки 1-го и других уровней (вложенность):
  ![t]()
  
  Таблицы БД после создания должны выглядеть так:
  ![f]()
  
  Получившиеся меню на странице:
  ![fi]()
  
 
### Требования к окружению:

* Python 3.7+;
* Django 3.0.3;
* Linux/Windows;

### Запуск:

1. `$ python manage.py makemigrations`,
2. `$ python manage.py migrate`,
3. `$ python manage.py createsuperuser`,
4. `$ python manage.py runserver`,
5. создать меню через Django-admin,
6. скорректировать названия меню в шаблоне main.html, которые задали в Django-admin,
7. задать URL-адрес(а) согласно созданной структуре меню
