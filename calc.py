def calculateAgain():
  calculate = 'yes'
  print('Do you want to perform a calculation? (yes or no)')
  calculate = str.lower(input()) 
  while calculate == 'yes' or calculate == 'y':
    doMath()
    if calculate != "yes" or  calculate !='y':
      break
    
#Creating function allows me to repeat it in while loop below.
def doMath():
    print("Choose operation (select number): ")
    print("1) addition")
    print("2) subtraction")
    print("3) multiplication")
    print("4) division")
    operation = input('')
    if(operation == "1" or operation == "2"
      or operation == "3" or operation == "4"):
      try:
        numOne = int(input("Select first number: "))
        numTwo = int(input("Select second number: "))
      except ValueError:
        print("You did not enter a valid number.")
        calculateAgain()
      else:
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
          if operation == "1":
              print(add(numOne, numTwo))
              calculateAgain()
          elif operation == "2":
              print(sub(numOne, numTwo))
              calculateAgain()
          elif operation == "3":
              print(mult(numOne, numTwo))
              calculateAgain()
          elif operation == "4":
              print(div(numOne, numTwo))
              calculateAgain()
          else:
              print("Sorry, something went awry!")
              calculateAgain()
    else:
      print("You did not select a valid operation.")
      calculateAgain()

doMath()