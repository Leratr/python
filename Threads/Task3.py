"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import threading
import time


def inputik():
    a=0
    while True:
        print("Введите быстрее")
        time.sleep(5)
        a+=1
        if a==15:
            print("Вы взорвались")
            break


def bomba():
    parol = input("\nВведите код: ")
    if parol == "балдеж":
        print("Бомба разминирована")
    else:
        print("Вы взорвались")

if __name__ == "__main__":
    thread = threading.Thread(target=inputik)
    thread.daemon = True
    thread.start()
    bomba()