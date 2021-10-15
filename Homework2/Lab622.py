num1 = int(input())
num2 = int(input())
answer1 = int(input())

num3 = int(input())
num4 = int(input())
answer2 = int(input())


def function1(x,y):
    return num1 * x + num2 * y - answer1
def function2(x,y):
    return num3 * x + num4 * y - answer2

x_val = 100
y_val = 100

for x in range(-10, 11):
    for y in range(-10,11):
        if function1(x,y) == function2(x,y) and function1(x,y) == 0:
            x_val = x
            y_val = y
if x_val != 100:
    print(x_val, y_val)
else:
    print('No solution')