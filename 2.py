'''Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

def pair_multy(nums: list[int]) -> list[int]:
    pairs = []
    iterations = (len(nums)+1)//2
    print(iterations)
    for i in range(iterations):
        pairs.append(nums[i]*nums[-1-i])
    return(pairs)
        
nums = [2, 3, 4, 5, 6]
print(pair_multy(nums))