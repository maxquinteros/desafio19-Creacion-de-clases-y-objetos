from te import Te

print(
    """Ingrese el sabor de su té
    1 - te negro
    2 - te verde
    3 - infusion de hierbas"""
)
sabor_usuario = int(input("> "))

print(
    """Ingrese el formato deseado
    1 - 300 gr
    2 - 500 gr"""
)
formato_usuario = int(input("> "))

print(f"El sabor de su té es: {Te.texto_sabor(sabor_usuario)}")
print(f"El formato de su té es: {formato_usuario}")
print(f"El precio de su té es: {Te.precio(formato_usuario)}")
print(f"El tiempo de preparación para su té es: {Te.tiempo_preparacion(sabor_usuario)}")
print(f"{Te.recomendacion(sabor_usuario)}")