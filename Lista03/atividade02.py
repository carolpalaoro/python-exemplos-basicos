# Lista usando o laço for
print(" ")
print("Lista dos Estados")
print(" ")

estados = ["São Paulo", "Minas Gerais", "Rio de Janeiro", "Espirito Santo"]

# Listar usando laço
for i, estado in enumerate(estados, 1):
    print(f"{i} - {estado}")