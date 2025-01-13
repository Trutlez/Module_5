class House:
    houses_history_init = []
    houses_history_new = []

    def __new__(cls, *args, **kwargs):
        if len(args) > 0:
            cls.houses_history_new.append(args[0])
        else:
            cls.houses_history_new.append(kwargs['name'])
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors
        House.houses_history_init.append(name)

    def __del__(self):
        print(f'{self.name} снесен, но остается в истории.')

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        else:
            print(f'Аргумент {value} не является ни домом, ни целым числом')
        return self

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        return self + value

    def __mul__(self, value):
        if isinstance(value, int):
            self.number_of_floors *= value
        elif isinstance(value, House):
            self.number_of_floors *= value.number_of_floors
        else:
            print(f'Аргумент {value} не является ни домом, ни целым числом')
        return self

    def __rmul__(self, value):
        return self * value

    def __imul__(self, value):
        return self * value

class Example:

  def __new__(cls, *args, **kwargs):
    print(args)
    print(kwargs)
    return object.__new__(cls)

  def __init__(self, first, second, third):
    print(first)
    print(second)
    print(third)

ex = Example('data', second=25, third=3.14)
print('-----------')

# Пример результата выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history_init)
h2 = House('ЖК Акация', floors=20)
print(House.houses_history_init)
h3 = House(name='ЖК Матрёшки', floors=20)
print(House.houses_history_init)

# Удаление объектов
del h2
del h3

print(House.houses_history_init)
print(House.houses_history_new)
