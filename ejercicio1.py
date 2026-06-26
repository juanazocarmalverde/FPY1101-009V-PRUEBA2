PRECIO_MEDICAMENTOS = 60000
PRECIO_DESPACHO = 8000

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C o D): ").upper()

# --- Descuento medicamentos ---
descuento_med = 0

if edad <= 30:
    if tramo in ("A", "B"):
        descuento_med = 0.18
    elif tramo in ("C", "D"):
        descuento_med = 0.12
elif 31 <= edad <= 60:
    if tramo in ("A", "B"):
        descuento_med = 0.12
    elif tramo in ("C", "D"):
        descuento_med = 0.08
# edad > 60 → descuento_med queda en 0

valor_medicamentos = int(PRECIO_MEDICAMENTOS * (1 - descuento_med))

# --- Descuento despacho ---
descuento_despacho = 0

if tramo in ("A", "B"):
    descuento_despacho += 0.10
    if edad >= 55:
        descuento_despacho += 0.05

valor_despacho = int(PRECIO_DESPACHO * (1 - descuento_despacho))

print("El valor de medicamentos es:", valor_medicamentos)
print("El valor del despacho es:", valor_despacho)
