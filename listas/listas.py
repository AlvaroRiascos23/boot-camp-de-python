to_do = ["Alistar la pelicula",
         "Freir la maispira",
         "Preparar pasabocas"]
print(to_do)

dia_hoy = ["Reunion 7:30 am",
         "Inicio trabajo 8:00 am",
         "pausa 11: 30 am",
         "Inicio trabajo 2:00pm",
         "Inicio Clases 6:00pm"]
print(dia_hoy)
numbers = [1,2,3,4, "cinco"]
print(numbers)
print(type(numbers))
mix = ["uno",2,3.14,True,[1,2,3]]
print(mix)
print(len(mix))
print("primer elemento:", mix[0])
print("elemento dos:", mix[1])
print("primer elemento:", mix[0])
print("elemento dos:", mix[1])
print(mix[2:-2])
print(mix[2:len(mix)])
mix.append(False)
mix.append("Alvaro")
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1,2,100,90.45,3,4,5]
print(numbers)
print("Mayor", max(numbers), "Menor", min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del(numbers)