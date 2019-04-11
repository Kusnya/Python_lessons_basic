# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print("Задача 1: ")
print()


def fibonacci(first, last):
    res = []
    num1 = 0
    num2 = 1
    for i in range(last + 1):
        if i >= first: res.append(num2)
        num1, num2 = num2, num2 + num1
    return res


fst = int(input("Введите номер первого элемента: "))
lst = int(input("Введите номер второго элемента: "))
print(fibonacci(fst, lst))

print()
print(30 * "-")

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print("Задача 2: ")
print()


def sort_to_max(origin_list):
    res = origin_list[:]
    for i in range(1, len(origin_list)):
        j = i
        while (res[j] < res[j - 1]) and (j > 0):
            res[j], res[j - 1] = res[j - 1], res[j]
            j -= 1
    return res


list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print("Исходный список:        ", list)
print("Отсортированный список: ", sort_to_max(list))

print()
print(30 * "-")

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print("Задача 2: ")
print()


def my_filter(func, iter):
    res = []
    for i in iter:
        if func(i):
            res.append(i)
    return res


def my_iter_filter(func, iter):
    for i in iter:
        if func(i):
            yield i


print("Исходный список: [-1, 2, 4, -8, 0, 6], фильтруется по правилу: значение >= 0")
print("Отфильтрованный список: ", my_filter(lambda x: x >= 0, [-1, 2, 4, -8, 0, 6]))
print()
print("Исходный список: [-1, 2, 4, -8, 0, 6], фильтруется по правилу: значение >= 5")
print("Отфильтрованный список: ", my_filter(lambda x: x > 5, [-1, 2, 4, -8, 0, 6]))

print()
print(30 * "-")

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print("Задача 4: ")
print()


def parallelogramm(a1, a2, a3, a4):
    def central(a, b):
        return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

    if a1 == a3:
        return "не является параллелограмом"
    elif central(a1, a3) == central(a2, a4):
        return "является параллелограмом"


print("Фигура с вершинами:", (1, 1), (1, 1), (1, 1), (1, 1), parallelogramm((1, 1), (1, 1), (1, 1), (1, 1)))
print("Фигура с вершинами:", (0, 0), (2, 2), (8, 2), (6, 0), parallelogramm((0, 0), (2, 2), (8, 2), (6, 0)))
