import csv
from datetime import date
import os
from django.conf import settings

class registroCSV:
  def __init__(self, usuario=None, password=None, nombre=None, correo=None, telefono=None):
    self.usuario = usuario
    self.password = password
    self.nombre = nombre
    self.correo = correo
    self.telefono = telefono
    self.curso = None
    self.empresa = None
    self.estado_curso = None
    self.estado_registro = None
    self.fecha_registro = None
    #self.miarchivoCSV = 'miregistro.csv'
    self.miarchivoCSV = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'miregistro.csv')

  def __str__(self):
    return f"usuario: {self.usuario} \npassword: {self.password} \nnombre: {self.nombre} \ncorreo: {self.correo} \ntelefono: {self.telefono} \ncurso: {self.curso} \nempresa: {self.empresa} \nestado del curso: {self.estado_curso} \nestado del registro: {self.estado_registro} \nfecha de registro: {self.fecha_registro}"

  def obtener_filas_csv(self):
    resultado = []
    with open(self.miarchivoCSV, 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
        resultado.append(row)
    return resultado

  def abrirCSV(self):
    with open(self.miarchivoCSV,'r') as fileOpen:
      reader = csv.reader(fileOpen)
      for row in reader:
        print(row)
      fileOpen.close()

  def buscar_en_csv(self, valor_a_buscar):
    with open(self.miarchivoCSV, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if valor_a_buscar in row:
                return  True  # Detiene la busqueda despues de encontrar la primer coincidencia.
    return False

  def nuevo_registro(self):
    with open(self.miarchivoCSV, 'a') as file:
      writer = csv.writer(file)
      writer.writerow([self.usuario, self.password, self.nombre, self.correo, self.telefono, self.curso, self.empresa, self.estado_curso, self.estado_registro, self.fecha_registro])
      file.close()

  def registro_vacio(self):
    with open(self.miarchivoCSV, 'r') as file:
      reader = csv.reader(file)
      fila_numero = 0
      for row in reader:
        if row[3] == '': # indice 3 es la columna correo
          return fila_numero
        fila_numero += 1
    return -1 # si no hay correo vacio

  def actualizar_fila(self,indice_fila):
    rows = []
    with open(self.miarchivoCSV, 'r') as file:
      reader = csv.reader(file)
      for row in reader:
        rows.append(row)

    if indice_fila >= 0 and indice_fila < len(rows):
      rows[indice_fila][2] = self.nombre  # indice 2 es la columna nombre
      rows[indice_fila][3] = self.correo  # indice 3 es la columna correo
      rows[indice_fila][9] = date.today()  # indice 9 es la columna fecha registro

    with open(self.miarchivoCSV, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(rows)
      file.close()
