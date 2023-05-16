# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint as RI

min_limit = 0
max_limit = 1000
hidden_number = RI(min_limit, max_limit)
print(f'Скажу по секрету... CPU загадал {hidden_number}')
my_number = None
attempt = 0

while my_number != hidden_number:
    print('- Я думаю, что это число... ', end=' ')
    my_number = (max_limit + min_limit) // 2
    print(my_number)
    if my_number > hidden_number:
        print('- Нет, мое число меньше')
        max_limit = my_number
    else:
        print('- Моё число больше')
        min_limit = my_number
    attempt += 1

print(f'Я угадал число {my_number} с {attempt} попытки')