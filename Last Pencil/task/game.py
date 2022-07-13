print('How many pencils would you like to use:')
num_1 = int(input())

print('Who will be the first (John, Jack)')
user = input()

multi = '|' * num_1
print(multi)
print(f"{user}'s turn")
turn = "Jack's"

while num_1 > 0:


    if user == 'John':
        if num_1 >= 1:
            number = int(input())
            num_1 -= number
            number_pencils = num_1 * '|'
            if num_1 >= 1:
                print(number_pencils)
                print("Jack's turn:")

    if turn == "Jack's":
        if num_1 >= 1:
            number = int(input())
            num_1 -= number
            number_pencils = num_1 * '|'

            if num_1 >= 1:
                print(number_pencils)
                print("John's turn:")
        user = "John"