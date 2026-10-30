'''Un hospital requiere 1 sistema que tenga 2 opciones, estas 2 opciones son: 
mensaje de bienvenida debe mostrar el proposito del sistema

(variables, menú y forma de escribir debe ser igual)
(mayoría de edad 15 años >= )

1- registros de pacientes por su nombre completo, el cual requiere almacenar como máximo 10 elementos (formato es en minúscula,}
separado con espacios (en español))
regla: trabajo de 2, los duos del lado izquierdo es el que hará la opción 1
   
2- registrar una lista de trabajadores del hospital, el cual como máximo debe ser 20 elementos y solo si es mayor de edad
se va a registrar el estado de los trabajadores
regla: cada dúo solo tendrá 1 repositorio de GitHub (Los trabajos se unificaran en GitHub
regla: El menú debe aceptar solamente opción 1,  y 3 (salir), cualquier otra opción se repetirá la pregunta'''

paciente = []
contador_pacientes = 0
confirmar = 2

while (confirmar == 2):
    print("Bienvenido al sistema de registro del hospital")
    print("==============================================")
    print(f"1) registrar pacientes [Total ingresados: {contador_pacientes}/10]")
    print("2) registrar lista trabajadores")
    print("3) salir")
    print()

    while True:
        try:
            opcion = int(input("Selecciona la opción (1-3): "))
            if 1 <= opcion <= 3:
                break
            print("Opción inválida. Debe ser entre 1 y 3.")
        except ValueError:
            print("Error: ¡Debes ingresar un número entero, no letras!")

    match opcion:
            case 1:
                print()
                print("  Registrar paciente  ")
                print("======================")
                if contador_pacientes >= 10:
                    print("Error, se ha alcanzado el limite de ingresos")
                    print()
                else:
                    registro_paciente = input("Ingrese su nombre completo: ").lower()
                    paciente.append(registro_paciente)

                    contador_pacientes += 1
                    print(f"Paciente ingresado correctamente. (Total ingresados: {contador_pacientes}/10)")
                    print() 
            case 2:
                print()
            case 3:
                print("Quieres salir? 1) Sí  2) No")
                while True:
                    try:
                        confirmar = int(input("Selecciona una opción (1-2): "))
                        if 1 <= confirmar <= 2:
                            break
                        print("Opción invalida")
                    except ValueError:
                        print("Queri salir? 1) Sí  2) No")
                        confirmar = int(input("Responda: "))
            case _:
                print("Dato incorrecto")