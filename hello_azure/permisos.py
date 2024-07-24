import os

def verificar_permisos(ruta_archivo):
  permisos = oct(os.stat(ruta_archivo).st_mode)[-3:]
  print(f"Permisos del archivo {ruta_archivo}: {permisos}")
  if int(permisos[0]) >= 4:
    print("El archivo tiene permisos de lectura para el propietario.")
  else:
    print("El archivo NO tiene permisos de lectura para el propietario.")

verificar_permisos('miregistro.csv')