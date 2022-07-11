# put your python code here
num_1 = float(input())
num_2 = float(input())
arithmetic = input()

if num_2 == 0.0 and arithmetic in ["mod", "div", "/"]:
    print('Division by 0!')
elif arithmetic == "mod":
    print(num_1 % num_2)
elif arithmetic == "pow":
    print(num_1 ** num_2)
elif arithmetic == "div":
    print(num_1 // num_2)
elif arithmetic == "+":
    print(num_1 + num_2)
elif arithmetic == "-":
    print(num_1 - num_2)
elif arithmetic == "*":
    print(num_1 * num_2)
elif arithmetic == "/":
    print(num_1 / num_2)