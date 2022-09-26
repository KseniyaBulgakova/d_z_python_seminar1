day = int(input('Введите номер: '))
if day > 7 or day < 1:
    print('Введите другое число')
elif day == 6 or day == 7:
    print("Да")
else:
    print("Нет")