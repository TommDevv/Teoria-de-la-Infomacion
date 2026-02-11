import math

value: int
inunit: str
outunit: str
output_value: int

unidades = {
    "1":{ "nombre": "bit", "base": 2 },
    "2":{ "nombre": "nat", "base": math.e },
    "3":{ "nombre": "Hartley", "base": 10 }
}

def info_units_conversion(input_unit, output_unit, value):
    if input_unit == output_unit:
        return value
    w = math.log(input_unit, output_unit)
    global conv_factor
    conv_factor = w
    return value*w


print("====================================")
print("   Seleccione la unidad de entrada  ")
print("====================================")
for clave, valor in unidades.items():
    print(f"{clave}. {valor['nombre'].capitalize()}")

opcion = input("Escriba 1, 2 o 3 y presione Enter: ")

inunit = unidades.get(opcion)

if inunit:
    print("Unidad seleccionada:", inunit["nombre"])
else:
    print("Opción no válida.")

print("\n====================================")
print("   Seleccione la unidad a Convertir   ")
print("====================================")
for clave, valor in unidades.items():
    print(f"{clave}. {valor['nombre'].capitalize()}")

opcion_out = input("Escriba 1, 2 o 3 y presione Enter: ")

outunit = unidades.get(opcion_out)

if outunit:
    print("Unidad seleccionada:", outunit["nombre"])
else:
    print("Opción no válida.")

value = int(input("Ingrese el valor a convertir: "))

if inunit == outunit:
    output_value = value
    print("La unidad de entrada y salida son iguales, el valor ingresado es:", output_value)
else:
    output_value = info_units_conversion(inunit['base'], outunit['base'], value)
    print(f"{value} {inunit['nombre']}s es igual a {output_value} {outunit['nombre']}s")
    print(f"El factor de conversión es: {conv_factor}")
