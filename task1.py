# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
#
# 6 12

lenN = int(input("enter count N: "))
lenM = int(input("enter count M: "))
n = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
m = [3, 6, 9, 12, 15, 18]
_set = set()

for i in range(lenN):
    n.append(int(input(f"enter value N {i + 1}/{lenN}: ")))
print(n)
for i in range(lenM):
    m.append(int(input(f"enter value M {i + 1}/{lenM}: ")))
print(m)

if lenN > lenM:
    for i in range(lenM):
        for j in range(lenN):
            if m[i] == n[j]:
                _set.add(n[j])
else:
    for i in range(lenN):
        for j in range(lenM):
            if n[i] == m[j]:
                _set.add(m[j])

print(*sorted(list(_set)))