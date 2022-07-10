print('How many pencils would you like to use:')
num_1 = int(input())

print('Who will be the first (John, Jack)')
user = input()

if user == 'John':
    print(num_1 * "|")
    print(user + " is going first")
elif user == 'Jack':
    print(num_1 * "|")
    print(user + " is going first")
