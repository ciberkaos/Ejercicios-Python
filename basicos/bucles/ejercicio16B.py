contrasena_correcta = "python123"
ok = False

while not ok:
    contrasena_usuario = input("Dame una contraseña: ")
    if contrasena_correcta == contrasena_usuario:
        print("Correcto")
        ok = True  # 'True' debe estar en mayúscula
    else:
        print("Contraseña incorrecta")


