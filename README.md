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
  
  ![f](https://github.com/Padking/tree_menu/blob/master/screenshots/create_menu.JPG)


  Создать заголовок 0-го уровня (корень меню):
  ![s](https://github.com/Padking/tree_menu/blob/master/screenshots/create_root.jpg)
  
  Создать заголовки 1-го и других уровней (вложенность):
  ![t](https://github.com/Padking/tree_menu/blob/master/screenshots/create_1st_section.jpg)
  
  Таблицы БД после создания должны выглядеть так:
  ![f](https://github.com/Padking/tree_menu/blob/master/screenshots/DB_after_section.JPG)
  ![fi](https://github.com/Padking/tree_menu/blob/master/screenshots/DB_after_menu.JPG)
  
  Получившиеся меню на странице:
  ![si](https://github.com/Padking/tree_menu/blob/master/screenshots/final_menu.JPG)
  
 
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
