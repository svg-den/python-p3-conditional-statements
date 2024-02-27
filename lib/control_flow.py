def admin_login(username, password):
    if(username.lower()== "admin" or username.upper() == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
print(admin_login("admin", "12345"))
print(admin_login("ADMIN", "12345"))
print(admin_login("adminn", "12345"))
pass

def hows_the_weather(temperature):
    if(temperature < 40):
        return "It's brisk out there!"
    elif(temperature >= 40 and temperature <= 65):
        return "It's a little chilly out there!"
    elif(temperature < 85):
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"
print(hows_the_weather(35))
print(hows_the_weather(75))
print(hows_the_weather(99))
print(hows_the_weather(100))
pass

def fizzbuzz(number):
    if(number % 3 == 0 and number % 5 == 0 ):
      return("FizzBuzz")
    elif number % 3 == 0:
      return("Fizz")
    elif number % 5 == 0:
      return ("Buzz")
    else:
      return (number)  

print(fizzbuzz(15))
print(fizzbuzz(33))
print(fizzbuzz(50))
print(fizzbuzz(0))
print(fizzbuzz(13))
pass

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
       print("Invalid operation!")
       return None
    
print(calculator("+", 5, 3))   
print(calculator("-", 10, 4))  
print(calculator("*", 7, 2))   
print(calculator("/", 8, 0))   
print(calculator("nope", 4, 2))   
pass