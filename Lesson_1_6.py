while True:
    start_km = float(input("Ваш начальный результат: "))
    finish_km = float(input("Желаемый финишный результат: "))
    deys = 1
    if start_km <= 0 or finish_km < 0:
        print("Результат должен быть больше 0! Стартовое значение должно быть больше 0!")
    else:
        while start_km <= finish_km:
            if start_km == finish_km:
                break
            start_km += start_km/10
            deys += 1
            print(f"Вы добъетесь результата за {deys} дней")
            break
            