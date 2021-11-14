time = int(input("Введите время в секудах от 0 до 86 400: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"Время в формате чч:мм:сс - {hours:02}:{minutes:02}:{seconds:02}")


