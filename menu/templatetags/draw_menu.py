from django import template
from menu.models import Menu, MenuItem

# Создание переменной для регистрации тега "draw_menu"
register = template.Library()

# Процедура регистрации тега 'draw_menu' для одноимённого шаблона
@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
	""" Определяет пользовательский тег
	:return: словарь - контекст для шаблона
	"""
	current_item = get_current_item(context['request'])
	# Получение объекта из БД
	menu = Menu.objects.get(name=menu_name)
	START_LVL = 0
	# Берём только те пункты меню, у которых поле lvl=START_LVL
	menuitems = list(menu.all_items.filter(lvl=START_LVL))
	if current_item.menu == menu:
		menuitems = expand_menu_until(menuitems, current_item)
	return {"menuitems": menuitems, "menu": menu}
	
def expand_menu_until(zero_lvl_items, until_item, expand_menu_items=None):
	"""Разворачивает пункты меню

	:param zero_lvl_items: список пунктов меню нулевого уровня
    :param until_item: номер пункта, до которого нужно развернуть меню
	:return: объект развёрнутого меню типа list
    """
	START_LVL = 0
	queue = zero_lvl_items
	expand_menu_items = expand_menu_items or []
	lvl = START_LVL
	while len(queue) > 0:
		item = queue.pop(0)
		lvl_dif = lvl - item.lvl
		if lvl_dif > 0:
            # При генерации шаблона вместо "out" будет вставлен закрывающий тег </ul>
			html_li = "out"
		elif lvl_dif < 0:
			html_li = "in"
		expand_menu_items.extend([html_li for _ in range(abs(lvl_dif))]) 
		lvl = item.lvl
		expand_menu_items.append(item)
		if lvl < until_item.lvl or item == until_item:
			queue += list(item.menuitem_set.all())
	expand_menu_items.extend([html_li for _ in range(abs(lvl))])
	return expand_menu_items

def get_current_item(request):
	""" Получает запрошенный пункт меню пользователем из объекта-запроса"""
	current_item = MenuItem.objects.get(url=request.path)
	return current_item