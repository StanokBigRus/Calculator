from math import *


print("Hello, My dear Brothers. Today I am pleased to present you a mini-calculator.\n"
      "You can use the whole math set of the development environment.\n"
      "If you enter incorrect data, the application will notify you. The application will prompt you to enter a new expression each time.\n"
      "Type 'exit' or 'quit' to exit the program.\n"
      "")
while True:
   try:
      inexp = input('Enter an expression :\n')
      inexp = inexp.lower()
      if inexp.replace(" ","") in {"quit", "exit"}:
         raise SystemExit()
      print(eval(inexp))
   except (TypeError, NameError, SyntaxError, ZeroDivisionError):
      print("Expression entered incorrectly")





