import time
import random
import sys
import os
from datetime import datetime

import colorama
from progress.bar import IncrementalBar
from colorama import *


def logo():
    print('Initializing...')
    time.sleep(1.3)

    bar = IncrementalBar('Подключение к серверам:', max=100)
    for _ in range(1, 101):
        bar.next()
        time.sleep(0.03)
    bar.finish()
    time.sleep(0.7)
    bar = IncrementalBar('Загрузка Базы Данных:  ', max=100)
    for _ in range(1, 101):
        bar.next()
        time.sleep(0.03)
    bar.finish()
    time.sleep(0.9)
    bar = IncrementalBar('Идет анализ:           ', max=100)
    for _ in range(1, 101):
        bar.next()
        time.sleep(0.05)
    bar.finish()

    os.system('cls||clear')

    # art = text2art("AVIATOR", font='block', chr_ignore=True, decoration='#')
    # tprint("        AVIATOR       ", font='banner3-d')
    time.sleep(0.5)
    print()
    print('\033[1m'+'                             ###     ##     ##  ####     ###     ########   #######   ######## '+'\033[0m')
    print('\033[1m'+'                            ## ##    ##     ##   ##     ## ##       ##     ##     ##  ##    ## '+'\033[0m')
    print('\033[1m'+'                           ##   ##   ##     ##   ##    ##   ##      ##     ##     ##  ##     ##'+'\033[0m')
    print('\033[1m'+'                          ##     ##  ##     ##   ##   ##     ##     ##     ##     ##  ######## '+'\033[0m')
    print('\033[1m'+'                          #########   ##   ##    ##   #########     ##     ##     ##  ##   ##  '+'\033[0m')
    print('\033[1m'+'                          ##     ##    ## ##     ##   ##     ##     ##     ##     ##  ##    ## '+'\033[0m')
    print('\033[1m'+'                          ##     ##     ###     ####  ##     ##     ##      #######   ##     ##'+'\033[0m')
    print(Style.BRIGHT + '                                                                            created by SINISTER')
    main()


def main():
    time.sleep(1)
    print()
    print(Fore.GREEN + Style.BRIGHT + '1.Сгенерировать' + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + '2.Выйти' + Style.RESET_ALL)
    print()
    x = int(input(Style.BRIGHT + 'Выбрать опцию: '))
    if x == 1:
        bar = IncrementalBar('Генерация:  ', max=100)
        for _ in range(1, 101):
            bar.next()
            time.sleep(0.06)
        bar.finish()

        number = random.uniform(1.6, 3.0)
        coeff = (round(number, 2))

        tm = datetime.now()
        min = random.randint(4, 11)

        prob_normal = random.randint(78, 90)
        prob_min = random.randint(65, 75)

        o = tm.minute + min
        if o >= 60:
            print()
            time.sleep(1)
            if coeff >= 2.2:
                print()
                print(Fore.MAGENTA + Style.BRIGHT + f'          Коэффициент: x{coeff}' + Style.RESET_ALL)
                time.sleep(1)
                print(
                    Fore.GREEN + Style.BRIGHT + f'          Время:       {tm.hour}:{tm.minute}' + Style.RESET_ALL)
                time.sleep(1)
                print(Fore.BLUE + Style.BRIGHT + f'          Вероятность: {prob_min}%' + Style.RESET_ALL)
                time.sleep(1)
                print()
            else:
                print()
                print(Fore.MAGENTA + Style.BRIGHT + f'          Коэффициент: x{coeff}' + Style.RESET_ALL)
                time.sleep(1)
                print(
                    Fore.GREEN + Style.BRIGHT + f'          Время:       {tm.hour}:{tm.minute}' + Style.RESET_ALL)
                time.sleep(1)
                print(Fore.BLUE + Style.BRIGHT + f'          Вероятность: {prob_normal}%' + Style.RESET_ALL)
                time.sleep(1)
                print()
        else:
            if coeff >= 2.2:
                print()
                dt_object2 = datetime.strptime(f"{tm.hour}:{tm.minute + min}:{00}", "%H:%M:%S")
                print(Fore.MAGENTA + Style.BRIGHT + f'          Коэффициент: x{coeff}' + Style.RESET_ALL)
                time.sleep(1)
                print(
                    Fore.GREEN + Style.BRIGHT + f'          Время:       {dt_object2.time().hour}:{dt_object2.minute}' + Style.RESET_ALL)
                time.sleep(1)
                print(Fore.BLUE + Style.BRIGHT + f'          Вероятность: {prob_min}%' + Style.RESET_ALL)
                time.sleep(1)
                print()
            else:
                print()
                dt_object2 = datetime.strptime(f"{tm.hour}:{tm.minute + min}:{00}", "%H:%M:%S")
                print(Fore.MAGENTA + Style.BRIGHT + f'          Коэффициент: x{coeff}' + Style.RESET_ALL)
                time.sleep(1)
                print(
                    Fore.GREEN + Style.BRIGHT + f'          Время:       {dt_object2.time().hour}:{dt_object2.minute}' + Style.RESET_ALL)
                time.sleep(1)
                print(Fore.BLUE + Style.BRIGHT + f'          Вероятность: {prob_normal}%' + Style.RESET_ALL)
                time.sleep(1)
                print()
        rand_sec = random.randint(6, 17)
        for i in reversed(range(0, rand_sec)):
            sys.stderr.write(Style.BRIGHT + f"Через {i:2d} сек, будет доступен следующий запрос. Ожидайте...\r")
            colorama.init()
            time.sleep(1)
        print()
        main()
    if x == 2:
        print()


if __name__ == '__main__':
    logo()