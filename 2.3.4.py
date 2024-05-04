# Caso 1: Consultar si una persona es mayor de edad
def verificar_edad(edad):
    if edad >= 18:
        return "Es mayor de edad"
    else:
        return "No es mayor de edad"

# Caso 2: Validar usuario y contraseña
def validar_usuario(usuario, contraseña):
    usuarios = {"pedro": "1234", "angel": "a4s1"}
    if usuario in usuarios and usuarios[usuario] == contraseña:
        return True
    else:
        return False

# Caso 3: Calcular promedio de 3 notas y determinar si está aprobado
def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    if promedio >= 4.0:
        return "Aprobado"
    else:
        return "Desaprobado"

# Caso 4: Pregunta sobre animales que viven en el agua y asignar puntaje
def preguntar_animal():
    print("¿Cuál de los siguientes animales vive en el agua?")
    print("a) Perro")
    print("b) Cocodrilo")
    print("c) Conejo")
    print("d) Tiburón")
    respuesta = input("Ingrese la letra correspondiente a su respuesta: ").lower()
    
    puntaje = 0
    if respuesta == "b":
        puntaje += 0.5
    elif respuesta == "d":
        puntaje += 1.0
    
    print("Puntaje obtenido:", puntaje)