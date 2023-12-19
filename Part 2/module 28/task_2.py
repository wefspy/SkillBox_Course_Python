# Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):
#     вычисление длины окружности,
#     вычисление площади окружности,
#     вычисление объёма куба,
#     вычисление площади поверхности сферы.

# Пример основного кода:
#     res_1 = MyMath.circle_len(radius=5)
#     res_2 = MyMath.circle_sq(radius=6)
#     print(res_1)
#     print(res_2)


class MyMath:
    """Статический класс, выполняющий математические вычисления"""
    @classmethod
    def circle_len(cls, radius: float) -> float:
        """Вычисление длины окружности

        Args:
            radius (float): радиус окружности

        Returns:
            float: длина окружности
        """
        return 2 * 3.14 * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """Вычисление площади окружности

        Args:
            radius (float): радиус окружности

        Returns:
            float: площадь окружности
        """
        return 3.14 * radius * radius

    @classmethod
    def cube_volume(cls, side: float) -> float:
        """Вычисление объёма куба

        Args:
            side (float): cторона куба

        Returns:
            float: объём куба
        """
        return side * side * side

    @classmethod
    def surface_area_sphere(cls, radius: float) -> float:
        """Вычисление площади поверхности сферы

        Args:
            radius (float): радиус сферы

        Returns:
            float: площадь поверхности сферы
        """
        return 4 * 3.14 * radius * radius
