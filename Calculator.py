from art import logo 


#Add
def addition(n1, n2):
  return n1 + n2

#Subtraction
def subtraction(n1, n2):
  return n1 - n2

#Multiplication
def multiplication(n1, n2):
  return n1 * n2

#Division
def Division(n1, n2):
  return n1 / n2

operations = {
  "+": addition,
  "-": subtraction,
  "*": multiplication, 
  "/": Division,
}
print(logo)

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations: 
    print(symbol)
  
  to_continue = True 
  while to_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"type 'y' to continue with {answer}, or type 'n' to start a  new calculation: ").lower() == "y":
      num1 = answer
    else: 
      should_continue = False
      calculator()

calculator()

    
