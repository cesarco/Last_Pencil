print('How many pencils would you like to use:')
num_1 = int(input())

print('Who will be the first (John, Jack)')
user = input()
multi = '|' * num_1
print(multi)
print(f"{user}'s turn")

while len(multi) > 0:
    user = input()
    if user == 'Jack':
        multi = multi[:num_1]
        print(multi[:])
        print("Jack's turn:")
    elif user == 'John':
        multi = multi[:num_1]
        print(multi[:])
        print("John's turn:")

