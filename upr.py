import json
import time as t

def main():
    try:
        pushups = int(input('Введите число отжиманий: '))
        squats = int(input('Введите число приседаний: '))
        abdominal = int(input('Введите число пресса: '))
    except Exception as e:
        print(f'Ошибка: {e}')
        pushups = int(input('Введите число отжиманий: '))
        squats = int(input('Введите число приседаний: '))
        abdominal = int(input('Введите число пресса: '))

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
            squats = int(input('Введите число приседаний: '))
            abdominal = int(input('Введите число пресса: '))
        except Exception as e:
            print(f'Ошибка: {e}')
            pushups = int(input('Введите число отжиманий: '))
            squats = int(input('Введите число приседаний: '))
            abdominal = int(input('Введите число пресса: '))

        total_squats.append(squats)
        total_pushups.append(pushups)
        total_abdominal.append(abdominal)

        sum_pushups = sum(total_pushups)
        sum_squats = sum(total_squats)
        sum_abdominal = sum(total_abdominal)


        print('Всего:')
        print(f'Отжиманий: {sum_pushups}')
        print(f'Приседаний: {sum_squats}')
        print(f'Пресса: {sum_abdominal}')


        with open("exersices.json", "w", encoding="utf-8") as f:
            json.dump([total_pushups, total_squats, total_abdominal], f)

if __name__ == "__main__":
    main()


