ingreso_mensual = 12000
ahorro_mensual = 6000
if ingreso_mensual > 10000:
    if ingreso_mensual < 7000:
        print("Ahora si estas bien")
    else:
        print("Estas gastando mucho, ahorra mas")
elif ingreso_mensual > 1000:
    print("Estas bien en cualquier parte del mundo")
elif ingreso_mensual > 500:
    print("Estas bien en Colombia")
elif ingreso_mensual > 200:
    print("Estas bien en Perú")
else:
    print("Estas en la pobreza")