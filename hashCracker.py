##Hay que corregir 

# import hashlib

# hash_file = "5d41402abc4b2a76b9719d911017c592"

# dic_file = input("Ingrese la direccion del archivo del diccionario: ")

# try:
#     with open(dic_file, "r") as file:
#         diccionario = [line.strip() for line in file]

#     encontrado = False
#     for password in diccionario:
#         hash_calculado = hashlib.sha256(password.encode()).hexdigest()
        
#         if hash_calculado == hash_file:
#             print("La contraseña original es: " + password)
#             encontrado = True
#             break
    
#     if not encontrado:
#         print("La contraseña no está en el diccionario")
# except FileNotFoundError:
#     print("El archivo del diccionario no se encontró. Por favor, verifica la ruta.")
