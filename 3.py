'''Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

List1 = list(map(float, input("Введите числа через пробел:\n").split()))

List2 = [round(i%1,5) for i in List1 if i%1 != 0]

print(f'Разница между максимальным и минимальным значением дробной части элементов равна {max(List2) - min(List2)}')