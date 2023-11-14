import random

operand = ["+", "-"]
min_operand = 1
max_operand = 50
problems = 10

input("Press enter to start!")
print("=================")


def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operand)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


for i in range(problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess != str(answer):
            print("FALSE👎")
            guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
            print("FALSE👎")
        else:
            print("GOOD👍")
            break
print("Well Done 🥳")

