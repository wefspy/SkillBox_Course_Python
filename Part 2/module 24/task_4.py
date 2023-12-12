# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый.
# У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
# Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».
#
# Таблица преобразований:
#     Вода + Воздух = Шторм;
#     Вода + Огонь = Пар;
#     Вода + Земля = Грязь;
#     Воздух + Огонь = Молния;
#     Воздух + Земля = Пыль;
#     Огонь + Земля = Лава.
#
# Напишите программу, которая реализует все эти элементы.
# Каждый элемент необходимо организовать как отдельный класс. Если результат не определён, то возвращается None.

class Element:
	def __init__(self, name):
		self.name = name

	def __add__(self, other):
		if isinstance(other, Element):
			if self.name and other.name in ('Вода', 'Воздух'):
				return Storm()
			elif self.name and other.name in ('Вода', 'Огонь'):
				return Steam()
			elif self.name and other.name in ('Вода', 'Земля'):
				return Mud()
			elif self.name and other.name in ('Воздух', 'Огонь'):
				return Lightning()
			elif self.name and other.name in ('Воздух', 'Земля'):
				return Dust()
			elif self.name and other.name in ('Огонь', 'Земля'):
				return Lava()
			else:
				return None
		else:
			return None


class Water(Element):
	def __init__(self):
		super().__init__('Вода')
	def __str__(self):
		return 'Вода'


class Air(Element):
	def __init__(self):
		super().__init__('Воздух')
	def __str__(self):
		return 'Воздух'

class Fire(Element):
	def __init__(self):
		super().__init__('Огонь')
	def __str__(self):
		return 'Огонь'

class Earth(Element):
	def __init__(self):
		super().__init__('Земля')
	def __str__(self):
		return 'Земля'

class Storm(Element):
	def __init__(self):
		super().__init__('Шторм')
	def __str__(self):
		return 'Шторм'

class Steam(Element):
	def __init__(self):
		super().__init__('Пар')
	def __str__(self):
		return 'Пар'

class Mud(Element):
	def __init__(self):
		super().__init__('Грязь')
	def __str__(self):
		return 'Грязь'

class Lightning(Element):
	def __init__(self):
		super().__init__('Молния')
	def __str__(self):
		return 'Молния'

class Dust(Element):
	def __init__(self):
		super().__init__('Пыль')
	def __str__(self):
		return 'Пыль'

class Lava(Element):
	def __init__(self):
		super().__init__('Лава')
	def __str__(self):
		return 'Лава'