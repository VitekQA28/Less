
'''
Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.
Например, передаем 2, на выходе получаем «Зима».
'''
def season(month):
    month = int(month)
    
    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"

month = input("Введите номер месяца: ")
print("Время года: "+season(month))