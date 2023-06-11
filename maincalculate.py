from math import * #Подключаем математический модуль


print("Hello, My dear Brothers. Today I am pleased to present you a mini-calculator.\n"
      "You can use the whole math set of the development environment.\n"
      "If you enter incorrect data, the application will notify you. The application will prompt you to enter a new expression each time.\n"      
      "Thank you for your creativity and for the best implementation of The Witcher. I hope that I can join your ranks, because this is my dream. Witcher.\n\n"
      "Type 'exit' or 'quit' to exit the program.\n"
      "")
while True:
   try:
      inexp = input('Enter an expression :\n')
      inexp = inexp.lower()
      if inexp.replace(" ","") in {"quit", "exit"}: #Переводим в нижний регистр и проверяем на команды выхода(теперь нам не важно кол-во пробелов в командах и регистр вводимый пользователем)
         raise SystemExit()
      print(eval(inexp)) #Вычисляем выражение
   except (TypeError, NameError, SyntaxError, ZeroDivisionError): #Проверка на неккоректный ввод
      print("Expression entered incorrectly")





