import re

print("Welcome to Rodrigo's calculator")
print("Type 'quit' to exit")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter a equation:\n")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye!")
        run = False
    else:
        equation = re.sub('[^\d\+\-\*/]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print("The result is", previous)

while run:
    performMath()