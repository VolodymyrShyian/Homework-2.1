user_number = input('Enter a four-digit number: ')
comparison = user_number.isdigit() and len(user_number) == 4
number = int(user_number) if comparison else 0
number, thousands = divmod(number, 10)
number, hundreds = divmod(number, 10)
number, tens = divmod(number, 10)
units = number
not comparison and print('Error: the input must contain exactly 4 digits!')
comparison and print(units)
comparison and print(tens)
comparison and print(hundreds)
comparison and print(thousands)