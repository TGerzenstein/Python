import time

#Desafio 8 - Programación Orientada a Objetos;
#Grupo 7 

#Creacion de clase Usuario;
class Usuario:
    def __init__(self, id_usuario = 0, nombre = " ", apellido = " ", username = " ", email = " ", contrasenia = " ", fecha_registro = 0, avatar = " ", estado = False):
      self.id_usuario = id_usuario
      self.nombre = nombre
      self.apellido = apellido
      self.username = username
      self.email = email
      self.contrasenia = contrasenia
      self.fecha_registro = fecha_registro
      self.avatar = avatar
      self.estado = estado


    def get_username(self):
      return self.username

    def get_contrasenia(self):
      return self.contrasenia 
    
    def get_estado(self):
      return self.estado
    
    def set_estado(self,nuevo_estado):
      self.estado = nuevo_estado

    def login(self):
      login_username = input("Ingrese su username: ")  
      login_contrasenia = input("Ingrese su contraseña: ")
      if (login_contrasenia == self.get_contrasenia()) and (login_username == self.get_username()):
        print("Inició sesión.")
        print(f"Bienvenid@ {self.nombre}!") 
        self.set_estado(True)
      else:
        print("Ingreso incorrecto. Intente de nuevo.")


    def registrar_usuario(self):
      self.nombre = input("Ingrese nombre: ")
      self.apellido = input("Ingrese apellido: ")
      self.username = input("Ingrese username: ")
      self.email = input("Ingrese email: ")
      self.contrasenia = input("Ingrese contraseña: ")
      self.fecha_registro = int(time.time())
      self.avatar = input("Ingrese avatar: ")
      self.set_estado(False)


    def __str__(self):
      return str(self.nombre) + " " + str(self.apellido) + " " + str(self.username) + " " + str(self.email) + " " + str(self.contrasenia) + " " + str(self.fecha_registro) + " " + str(self.avatar)

#Creacion de clase Publico;
class Publico(Usuario):
    
    def __init__(self, id=0, nombre=" ", apellido=" ", username=" ", email=" ", contrasenia=" ", fecha_registro=0, avatar=" ", estado=False, es_publico = True):
      super().__init__(id, nombre, apellido, username, email, contrasenia, fecha_registro, avatar, estado)
      self.es_publico = es_publico

    
    def set_publico(self, nuevo_publico):
      self.es_publico = nuevo_publico

    def registrar_publico(self):
      self.nombre = input("Ingrese nombre: ")
      self.apellido = input("Ingrese apellido: ")
      self.username = input("Ingrese username: ")
      self.email = input("Ingrese email: ")
      self.contrasenia = input("Ingrese contraseña: ")
      self.fecha_registro = int(time.time())
      self.avatar = input("Ingrese avatar: ")
      self.set_estado(False)
      self.set_publico(True)

    def comentar(self):
      nuevo_comentario = input("Escriba su comentario: ")
      coment = Comentario(2, 10, 1, nuevo_comentario)  
      print(coment.get_comentario())

#Creacion de clase Colaborador;
class Colaborador(Usuario):
  def __init__(self, id_usuario=0, nombre=" ", apellido=" ", username=" ", email=" ", contrasenia=" ", fecha_registro=0, avatar=" ", estado=False, es_colaborador = True):
    super().__init__(id_usuario, nombre, apellido, username, email, contrasenia, fecha_registro, avatar, estado)
    self.es_colaborador = es_colaborador 


  def set_colaborador(self, nuevo_colaborador):
    self.es_colaborador = nuevo_colaborador

  def registrar_colaborador(self):
    self.nombre = input("Ingrese nombre: ")
    self.apellido = input("Ingrese apellido: ")
    self.username = input("Ingrese username: ")
    self.email = input("Ingrese email: ")
    self.contrasenia = input("Ingrese contraseña: ")
    self.fecha_registro = int(time.time())
    self.avatar = input("Ingrese avatar: ")
    self.set_estado(False)
    self.set_colaborador(True)
  
  def comentar_colaborador(self):
    comentario_colaborador = input("Realice su comentario: ")
    comentario1 = Comentario(6, 11, 14, comentario_colaborador)  
    print(comentario1.get_comentario())


  def publicar_colaborador(self):
    nuevo_titulo = input("Ingrese el título del artículo: ")
    nuevo_resumen = input("Ingrese descripción del artículo: ")
    nuevo_contenido = input("Realice su comentario: ")
    articulo1 = Articulo(1, 20, nuevo_titulo, nuevo_resumen, nuevo_contenido)
    print(articulo1.get_titulo())
    print(articulo1.get_resumen())
    print(articulo1.get_contenido())

#Creacion de la clase Artículo;
class Articulo:
    def __init__(self,id_articulo, id_usuario, titulo = " ", resumen = " ", contenido_articulo = " ", fecha_publicacion = 0, imagen = " ", estado = False):
      self.id_articulo = id_articulo
      self.id_usuario = id_usuario
      self.titulo = titulo
      self.resumen = resumen
      self.contenido_articulo = contenido_articulo
      self.fecha_publicacion = fecha_publicacion
      self.imagen = imagen
      self.estado = estado


    def get_titulo(self):
      return self.titulo
   
    def get_resumen(self):
      return self.resumen
    
    def get_contenido(self):
      return self.contenido_articulo

#Creacion de clase Comentario;
class Comentario:
    def __init__(self, id_comentario, id_articulo, id_usuario, contenido = " "):
      self.id_comentario = id_comentario
      self.id_articulo = id_articulo
      self.id_usuario = id_usuario
      self.contenido = contenido
      self.fecha_hora = int(time.time())
      self.estado = True

    def get_comentario(self):
      return self.contenido




#Instancias 

print(" ")
print("-------------- Login --------------")
persona1 = Usuario(1,"Maria","Martin","Mary","mary@gmail.com","HDVLM","12/05/2023",False)
persona1.login()

#Instancia para utilizar el método registrar usuario
print(" ")
print("-------------- Registrar usuario --------------")
persona2 = Usuario()
persona2.registrar_usuario()
print(f"Bienvenido {persona2.nombre} {persona2.apellido}.\n-> Su usuario {persona2.username} se ha registrado.")


#Registrar Publico
print(" ")
print("-------------- Registrar publico --------------")
persona4 = Publico()
persona4.registrar_publico()

#Instancia del Publico para utilizar comentar
print(" ")
print("-------------- Comentar publico --------------")
persona2 = Publico()
persona2.comentar()

#Instancia del Colaborador para comentar
print(" ")
print("-------------- Comentar colaborador --------------")
persona2 = Colaborador()
persona2.comentar_colaborador()

#Instancia del Colaborador para publicar
print(" ")
print("-------------- Publicar colaborador --------------")
persona3 = Colaborador()
persona3.publicar_colaborador()