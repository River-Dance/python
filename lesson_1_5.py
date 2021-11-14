income = float(input("Введите выручку компании: "))
expenses = float(input("Введите расходы компании: "))
result = income - expenses

if result > 0:
    print(f"Компания отработала с прибылью {result:.2f} руб")
    print(f"Рентабельность компании {100 * result / income:.1f} %")
    n_person = int(input("Сколько сотрудников в компании? "))
    print(f"Если вы разделите прибыль компании между сотрудниками, то каждый получит по - {result / n_person:.2f} руб")
elif result < 0:
    print(f"Компания отработала в убыток {result:.2f} руб")
else:
    print("Ноль прибыли, лучше чем убыток.")