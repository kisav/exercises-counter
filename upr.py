import json
import time as t

try:
    pushups = int(input('Введите число отжиманий: '))

    if pushups == -1:
        print('s')
        exit()
        print('a')
    elif pushups == -2:
        total_squats = []
        total_pushups = []
        total_abdominal = []
        pushups = int(input('Введите число отжиманий: '))

    squats = int(input('Введите число приседаний: '))
    abdominal = int(input('Введите число пресса: '))
except Exception as e:
    print(f'Ошибка: {e}')
    pushups = int(input('Введите число отжиманий: '))
    squats = int(input('Введите число приседаний: '))
    abdominal = int(input('Введите число пресса: '))
print('проверки прошли 1')

if pushups or squats or abdominal < -2:
    print('Ошибка входных данных. Попробуйте ещё раз.')
    pushups = int(input('Введите число отжиманий: '))
    squats = int(input('Введите число приседаний: '))
    abdominal = int(input('Введите число пресса: '))
print('проверки прошли')

try:
    with open("exersices.json", "r", encoding="utf-8") as f:
        total_pushups, total_squats, total_abdominal = json.load(f)
except json.JSONDecodeError:
    total_squats = []
    total_pushups = []
    total_abdominal = []
print('Opened')

total_squats.append(squats)
total_pushups.append(pushups)
total_abdominal.append(abdominal)
print('added')

while True:
    t.sleep(3)
    try:
        pushups = int(input('Введите число отжиманий: '))

        if pushups == -1:
            print('s')
            exit()
            print('a')
        elif pushups == -2:
            total_squats = []
            total_pushups = []
            total_abdominal = []
            pushups = int(input('Введите число отжиманий: '))

        squats = int(input('Введите число приседаний: '))
        abdominal = int(input('Введите число пресса: '))
    except Exception as e:
        print(f'Ошибка: {e}')
        pushups = int(input('Введите число отжиманий: '))
        squats = int(input('Введите число приседаний: '))
        abdominal = int(input('Введите число пресса: '))
    print('проверки прошли 1')

    if pushups or squats or abdominal < -2:
        print('Ошибка входных данных. Попробуйте ещё раз.')
        pushups = int(input('Введите число отжиманий: '))
        squats = int(input('Введите число приседаний: '))
        abdominal = int(input('Введите число пресса: '))
    print('проверки прошли')

    total_squats.append(squats)
    total_pushups.append(pushups)
    total_abdominal.append(abdominal)

    with open("exersices.json", "w", encoding="utf-8") as f:
        json.dump([total_pushups, total_squats, total_abdominal], f)






