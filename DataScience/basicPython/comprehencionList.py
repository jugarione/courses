evens = [x for x in range (1,100) if x%2 == 0]
print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transpose =[[row[i] for row in matrix] for i in range (len(matrix[0]))]
print(transpose)

lista = [1,2,3,4,5]
double =[i*2 for i in lista]
print(double)


#filtrar y transformr en un sol paso
lista2 = ["sol", "mar", "montaña", "rio", "estrella"]
plus3 = [x.upper() for x in lista2 if len(x)>3]
print(plus3)


listaclaves = ["nombre", "edad", "ocupación"]
listavalores = ["Juan", 30, "Ingeniero"]
diccionario = { listaclaves[i]:listavalores[i] for i in range(len(listaclaves))  }
print(diccionario)

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
madrileñosmas30 = [personas[i].get("nombre") for i in range(len(personas)) if personas[i].get("edad") > 30 and personas[i].get("ciudad") == "Madrid"]
print(personas[0].get("nombre"))
print(madrileñosmas30)

#conun else
numlist = [1,2,3,4,5,6,7,8,9,10]
doublepar = [x*2 if x%2==0 else x for x in numlist]
print(doublepar)
