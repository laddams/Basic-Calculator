from art import logo


#add 
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

#dictionary
operations = {
  "+" : add,
  "-" : subtract,
  "/" : divide,
  "*" : multiply,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
      print(symbol)
  
  keep_going = True
  
  while keep_going:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    operation = operations[operation_symbol]
    answer = operation(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    choice = input(f"Type 'y' to continue calculating with {answer}, otherwise type 'n' to start a new calculation: ")
    if choice == "n":
      keep_going = False
      calculator()
    else:
      num1 = answer
      

calculator()
  