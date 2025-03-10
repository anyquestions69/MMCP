from typing import List


def add_big_numbers(a:List[int], b:List[int], B:int) -> List[int]:
    n:int = len(a)
    c:int = 0  # Перенос
    w:List[int] = []  # Результат

    for i in range(n):
        t = a[i] + b[i] + c
        w.append(t % B)  # Текущий разряд
        c = t // B  # Перенос

    if c > 0:
        w.append(c)  # Добавляем последний перенос

    return w

def array_from_str(s:str) -> List[int]:
    return [int(char) for char in reversed(s)]


# Пример использования
a:List[int] = array_from_str("123456789")  # Число 456
b:List[int] = array_from_str("987654321") # Число 789
B:int = 10  # Основание системы счисления
print(a)
result = add_big_numbers(a, b, B)
print("Результат:", result)  # Вывод: [5, 4, 2, 1] (число 1245)