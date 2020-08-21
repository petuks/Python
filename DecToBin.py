print()
infinite_loop = 1
while infinite_loop == 1:
    print()
    number = input('Ievadi Dec skaitli:  ')
    print()
    decimal = int(number)
    binary = ''
    while decimal != 0:
        remainder = decimal % 2
        binary += str(remainder)
        decimal = int(decimal / 2)
    final_binary = binary[::-1]
    print("The binary is: " + (str(final_binary)))
    print()
