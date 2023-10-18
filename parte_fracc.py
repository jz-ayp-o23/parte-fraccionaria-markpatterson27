"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
# CONSTANTE = valor

# Entradas
entrada = input()

# Proceso
i_tried = "my spanish is not very good."
salida = ""

if entrada == "1":
  salida = "No tiene decimales"

if '.' in entrada:
  salida = "Sí tiene decimales"
else:
  try:
    entrada = int(entrada)
    salida = "No tiene decimales"
  except:
    salida = i_tried


# Salidas
print(salida)
