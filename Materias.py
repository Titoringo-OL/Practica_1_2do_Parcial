# Almacenar las materias de 1 curso (ejemplo Pensamiento matemático, español, Inglés, química, civismo y francés) en una lista luego despliegue en pantalla
print("Alvarez Delgdo Yael Ismael 3-W")
print(" ")
# Lista de materias
materias = [
    "Pensamiento matemático",
    "Leoye",
    "Inglés",
    "Humanidades",
    "Ecosistemas",
    "Programación"
]
print(materias)
print(" ")
# Mostrar materias y mensajes
for materia in materias:
    print(materia)
# De esa misma lista que aparezca un mensaje Estoy cursando <materia>, donde <materia> es cada una de las de la lista  .
    print(f"Estoy cursando {materia}.")
    # De igual forma con la lista que tenemos creada que pida al usuario la calificación de cada materia lo despliegue en pantalla y que muestre:
    # En <materia> has obtenido <calificación> y asíi cada una de las que correspondan
    calificacion = input(f"Ingrese la calificación para {materia}: ")
    print()  # Espacio adicional
    print(f"En {materia} sacaste {calificacion}.")
    print()  # Espacio adicional
