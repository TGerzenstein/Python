import time


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
       self.contrasenia = input("Ingrese contrasenia: ")
       self.fecha_registro = int(time.time())
       self.avatar = input("Ingrese avatar: ")
       self.set_estado(False)


persona1 = Usuario(1,"Maria","Martin","Mary","mary@gmail.com","HDVLM","12/05/2023",False)
persona1.login()

#persona2 = Usuario()
#persona2.registrar_usuario()


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
       self.contrasenia = input("Ingrese contrasenia: ")
       self.fecha_registro = int(time.time())
       self.avatar = input("Ingrese avatar: ")
       self.set_estado(False)
       self.set_publico(True)

    def comentar(self):
        nuevo_comentario = input("Realice su comentario: ")
        coment = Comentario(2, 10, 1, nuevo_comentario)  
        print(coment.get_comentario())
      


class Articulo:
    def __init__(self,id_articulo, id_usuario, titulo = " ", resumen = " ", contenido = " ", fecha_publicacion = 0, imagen = " ", estado = False):
      self.id_articulo = id_articulo
      self.id_usuario = id_usuario
      self.titulo = titulo
      self.resumen = resumen
      self.contenido = contenido
      self.fecha_publicacion = fecha_publicacion
      self.imagen = imagen
      self.estado = estado


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



#persona2 = Publico()
#persona2.comentar()