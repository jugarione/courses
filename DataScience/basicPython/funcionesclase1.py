def greet(name= "desconocido", last_name=""):
    print("Hola", name, last_name)

greet("julian", "garione")

def factorial(num):
    if num == 1:
        return 1
    else: 
        return num * factorial(num-1)

print(factorial(int(input("inserte un numero para saber el factorial: "))))
    
    
