# Se utiliza el try except para cuando un usuario
# intente ingresar un dato distinto de tipo int en este caso
# y evitar el error 'ValueError'. Ademas si el usuario ingresa
# un numero entero menor a 1, tendra que volver a ingresar un numero
# mayor o igual a 1.
print('How many pencils would you like to use: ')
while True:
    try:
        num_1 = int(input())
        if num_1 < 1:
            print('The number of pencils should be positive')
            True
        else:
            break

    except ValueError:
        print('The number of pencils should be numeric')

print("Who will be the first (John, Jack)")

usuario_1 = 'John'
usuario_2 = 'Jack'

user_input = input()
while True:
    if user_input == usuario_1 or user_input == usuario_2:
        multi = '|' * num_1
        print(multi)
        print(f"{user_input}'s turn")
        break
    else:
        print("Choose between 'John' and 'Jack'")
        user_input = input()

while num_1 > 0:
    try:
        number = int(input())
        while number >= 1 and number <= 3:
            if number <= num_1:
                num_1 -= number
                number_pencils = num_1 * '|'
                if num_1 > 0:
                    print(number_pencils)
                    if user_input == "John":
                        usuario_1, usuario_2 = usuario_2, usuario_1
                        print(f"{usuario_1}'s turn")
                    elif user_input == "Jack":
                        usuario_2, usuario_1 = usuario_1, usuario_2
                        print(f"{usuario_2}'s turn")
                    break
                else:
                    if user_input == "John":
                        print(f"{usuario_2} won!")
                    elif user_input == "Jack":
                        print(f"{usuario_1} won!")
                    break
            else:
                print('Too many pencils were taken')
                number = int(input())
        else:
            print("Possible values: '1', '2' or '3'")
    except ValueError:
        print("Possible values: '1', '2' or '3'")
