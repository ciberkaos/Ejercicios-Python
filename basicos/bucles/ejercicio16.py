contrasena_correcta = "python123"

while True:
    contrasena_usuario = input("dame una contrase~na")
    if contrasena_correcta == contrasena_usuario:
        print("correcto")
        break
    else:
        print("contrasena incorrecta")


