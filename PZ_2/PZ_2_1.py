

while True:
    try:
        number = int(input("введите трёхзначное число:"))
        if 100 <= number <= 999:
            break
        else:
            print("ошибка: нужно трёхзначное число.")
    except ValueError:
        print("ошиба: введите целое число, а не слова.")

hundreds = number // 100
tens= (number // 10) % 10
units = number % 10

new_number = tens * 100 + hundreds * 10 + units
print("новое число:", new_number)