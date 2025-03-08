#fibonacci
# 

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b #esto se ve de esta forma (a, b) = (b, a+b)

for num in fibonacci(20):
    print(num)


#ejemplo

mylist = [1,2,3,4]

my_iter = iter(mylist)

#uso el iterador
print(my_iter)

#itterador para numeros impares
limit = 50
# rangue(start, stop, step)
odd_itter = iter(range(1,limit+1,2))

for num in odd_itter:
    print(num)

#generador de pares

print("generador de pares")

def pares(limit):
    a, b = 0, 2
    while a < limit:
        yield a
        a, b = a+b, 2

for par in pares(50):
    print(par)



#generador de impares
print("generador de impares")

def impares(limit):
    a, b = 1, 2
    while a < limit:
        yield a
        a, b = a+b, 2

for impar in impares(50):
    print(impar)
