#1 Реализуйте алгоритм, который принимает массив и перемещает нули в конец, сохраняя порядок остальных элементов

def func(lst):
    my_lst = sorted(lst, key=lambda n: n == 0)
    return my_lst

#2 Посчитайте сумму н-го ряда пирамиды нечетных чисел (начало с 1)

def get_sum(n):
    res = 0
    start = n**2 - (n - 1)
    end = start + n * 2
    for i in range(start, end, 2):
        res += i
    return res
print(get_sum(4))