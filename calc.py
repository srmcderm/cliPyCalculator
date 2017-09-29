#Creating function allows me to repeat it in while loop below.
def doMath():
    prompt = print("Choose operation: addition, subtraction, multiply, or divide.")
    operation = input()
    numOne = input("Select first number: ")
    numTwo = input("Select second number: ")
#Error handling to check that input str can be converted to int.
#That way the whole program doesn't shut the user out.
    try:
        numOneInt = int(numOne)
        numTwoInt = int(numTwo)
    except ValueError:
        print("That is not an int!")
    if isinstance(numOneInt, int) and isinstance(numTwoInt, int):
 #All of the user defined functions to perform operations.
        def add(x, y):
            return x + y

        def sub(x, y):
            return x - y

        def mult(x, y):
            return x * y

        def div(x, y):
            return x / y
#Checking user string input to determine operation.x    
        if operation == 'addition':
            print(add(numOneInt, numTwoInt))
        elif operation == 'subtraction':
            print(sub(numOneInt, numTwoInt))
        elif operation == 'multiply':
            print(mult(numOneInt, numTwoInt))
        elif operation == 'divide':
            print(div(numOneInt, numTwoInt))
        else:
            print("Sorry, something went awry!")
#Function call to start calculator program.
doMath()
#Once program finishes, while loop will see if  you want to calculate again.
calculate = ''
print('Do you want to perform another calculation? (yes or no)')
calculate = input() 

while calculate == 'yes' or calculate == 'y':
    doMath()
else:
    print('See you next time!')