lista = ["Alvaro_Riascos", "tecnotutoriales Jheyson", True, 1.69]
print(lista[1])
lista[3] = "Alvarito"
print(lista[3])
tupla = ("Alvaro Riascos", "tecnotutoriales Jheyson", True, 1.69)
print(tupla[1])

#tupla[1] = "tips TIC al paso"
#print(tupla[1])

#creando conjunto o set
#Un conjunto no admite elementos duplicados
conjunto = {"Alvaro Riascos","tecnotutoriales Jheyson Galvis", True, 1.69}
print(conjunto)

#Creando un diccionario
diccionario = {
    "nombre" : "Alvaro",
    "apellido" : "Riascos",
    "estatura" : 1.69,
    "esta feliz" : True
}
print(diccionario["esta feliz"])
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["estatura"])
nombre = input("Digite su nombre ")
nombre_uno = int(nombre)

print(type(nombre_uno))