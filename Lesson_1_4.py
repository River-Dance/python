num_vvedenoe = int(input("Введите целое, положительное число: "))
peremen_max = 0
num = num_vvedenoe

while num > 0:
    digit = num % 10
    if digit > peremen_max:
        peremen_max = digit
    num = num // 10
print(f"Наибольшей цифрой в числе {num_vvedenoe}, является цифра {peremen_max}")
