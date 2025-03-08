# 1 = piedra, 2 = papel, 3 = tijeras
posibilidades = {"1-1":"emp", "1-2":"py2" , "1-3":"py1" , "2-1":"py1" , "2-2":"emp" , "2-3":"py2" , "3-1":"py2" , "3-2":"py1" , "3-3":"emp"}
print("las reglas son simples, 1 = piedra, 2 = papel, 3 = tijeras")
py1value = input("player 1, que elegis? 1, 2 o 3: ")
py2value = input("player 2, que elegis? 1, 2 o 3: ")
if posibilidades.get(py1value+"-"+py2value) == "emp": 
    print("empate")
elif posibilidades.get(py1value+"-"+py2value) == "py1":
    print("Gana player 1")
else: 
    print("Gana player 2")


