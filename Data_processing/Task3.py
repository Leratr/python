"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""
def print_pogoda(temperatura):
    for t in temperatura:
        print("Сегодня", t, "градусов")

temperatura = [25, 2, 14, 49]
print_pogoda(temperatura)