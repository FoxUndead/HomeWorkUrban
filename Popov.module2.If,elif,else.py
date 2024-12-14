first = int(input("Введите первое число:"))
second = int(input("Введите второе число:"))
third = int(input("Введите третье число:"))
if first == second == third:
    print(third)
elif first == second or second == third or third == first:
    print(second)
elif first != second or second != third or third != first:
    print(0)
