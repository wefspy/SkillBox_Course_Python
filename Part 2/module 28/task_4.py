# Создайте класс LRU Cache, который хранит ограниченное количество объектов и, при превышении лимита,
# удаляет самые давние (самые старые) использованные элементы.
# Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.
#
# @property
# def cache(self): # этот метод должен возвращать самый старый элемент
#
# @cache.setter
# def cache(self, new_elem): # этот метод должен добавлять новый элемент


from collections import deque
from typing import Any


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.__storage_keys = deque()
        self._cache = dict()

    @property
    def cache(self):
        oldest_key = self.__storage_keys[0]
        return self._cache[oldest_key]

    @cache.setter
    def cache(self, new_elm: tuple) -> None:
        if self.__storage_keys.__len__() >= self.__capacity:
            oldest_key = self.__storage_keys.popleft()
            del self._cache[oldest_key]

        self._cache[new_elm[0]] = new_elm[1]
        self.__storage_keys.append(new_elm[0])

    def get(self, key) -> Any:
        return self._cache.get(key)

    def print_cache(self):
        print(self._cache)


cache = LRUCache(2)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")

cache.print_cache()

print(cache.get("key2"))

cache.cache = ("key3", "value3")

cache.print_cache()
