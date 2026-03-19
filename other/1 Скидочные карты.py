# Задача: Очередь на кассу
# Платформа: Яндекс Контест
# 
# Условие:
# В очереди стоит N человек. Некоторые забыли скидочную карту (C человек),
# некоторые имеют запасную карту (R человек). Человек с запасной картой может
# поделиться ею с соседом. Найти максимальное количество людей,
# которые смогут воспользоваться скидочной картой.
#
# Ввод: N C R, затем список C и список R
# Вывод: максимальное количество людей со скидкой

N, C, R = map(int, input().split())
C_list = list(map(int, input().split()))
R_list = list(map(int, input().split()))

w_list = [1] * N

for i in range(N):
    if i+1 in C_list:
        w_list[i] -= 1
    if i+1 in R_list:
        w_list[i] += 1

for i in range(N):
    if w_list[i] == 0:
        if i > 0 and w_list[i-1] == 2:
            w_list[i] = 1
            w_list[i-1] = 1
        elif i < N-1 and w_list[i+1] == 2:
            w_list[i] = 1
            w_list[i+1] = 1

print(N - w_list.count(0))