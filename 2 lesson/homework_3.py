a = float(input("Ваш доход-->"))  # запрашиваем данные для переменных
b = float(input("Процент налога-->"))
print("Налогов к оплате:", round((a * b / 100), 2))  # подставляем переменные в формулу и выдаем результат
print("Чистый доход:", round((a - (a * b / 100)), 2))
