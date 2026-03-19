# Задача: Раскодируй строку
# Платформа: Яндекс Контест
#
# Условие:
# Шифр заменяет буквы на числа: a-i → 1-9, j-z → 10#-26#
# Например, "hello" → "8512#12#15#"
# Нужно раскодировать строку обратно.
#
# Ввод: закодированная строка
# Вывод: исходная строка из строчных латинских букв

code = input()
code = list(code)
i = 0
temp = 0
alphabet = list('abcdefghijklmnopqrstuvwxyz')
while i != len(code):
  if i < len(code)-2:
    if code[i+2] == '#':
      temp = int(str(code[i])+str(code[i+1]))
      i+=3
    else:
      temp = int(code[i])
      i+=1
  else:
    temp = int(code[i])
    i+=1
  print(alphabet[temp-1], end='')
  temp=0