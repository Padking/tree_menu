from django.core.exceptions import ValidationError
from django.db import models



class Menu(models.Model):
	name = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return self.name

class MenuItem(models.Model):
	""" Пункт в иерархической структуре меню"""

	# Определение полей модели (таблицы БД)
	title = models.CharField(max_length=200) # можно использовать параметр db_index=True - более быстрый поиск в БД
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, help_text="Выберите из выпадающего списка родителя для потомка, указанного в 'title'")
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True, related_name="all_items", help_text="Выберите из выпадающего списка меню для 0-го уровня")
	url = models.CharField(max_length=200, blank=True, null=True, help_text="Создаётся автоматически при заполнении 'title'")
	lvl = models.IntegerField(default=0, editable=False)

	# Переопределение метода .save, т.к. сохраняется экземпляр модели при условиях, описанных ниже
	def save(self):
		if self.parent:
			self.menu = self.parent.menu
			if not self.url:
				self.url = f"{self.parent.url}/{self.title}"
			self.lvl = self.parent.lvl + 1
		else:
			if not self.url:
				self.url = f"/{self.title}"
			self.lvl = 0
		if not self.parent and not self.menu:
			raise ValidationError("<Здесь текст при исключении>")
		super().save()
	# Организация вывода информации об экземпляре модели в более удобном виде
	def __str__(self):
		return f"Title: {self.title} | URL: {self.url} | Menu name: {self.menu}"