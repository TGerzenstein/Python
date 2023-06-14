#atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado
# métodos: login(), registrar()


class Usuario:
    def __init__(self,id,nombre,apellido,username,email,contrasenia,fecha_registro,avatar,estado):
      self.id = id
      self.nombre = nombre
      self.apellido = apellido
      self.username = username
      self.email = email
      self.__contrasenia = contrasenia
      self.fecha_registro = fecha_registro
      self.avatar = avatar
      self.estado = estado


def menu():
    print("""
    ¡Bienvenido al blog!
    MENU:
    1 -> 
    2 -> 
    0 -> Salir
    """)

    def login(self):
        login_username = input("Ingrese su username: ")  
        login_contrasenia = input("Ingrese su contraseña: ")
        if (login_contrasenia == self.__contrasenia) and (login_username == self.username):
          print("Inició sesión.")
          print(f"Bienvenid@ {self.nombre}!") 
          self.estado = True
        else:
           print("Ingreso incorrecto. Intente de nuevo.")



"""     def registrar_usuario(self):
        
        lista_usuarios = []
        id = int(input("Ingrese ID: "))
        nombre = input("Ingrese nombre de usuario: ").capitalize()
        apellido = input("Ingrese apellido de usuario: ").capitalize()
        username = input("Ingrese username de usuario: ")
        email = input("Ingrese correo electrónico: ")
        contrasenia = input("Ingrese su contraseña: ")
        self.nuevo_usuario = {    
        'id': id,                                             
        'nombre': nombre,
        'apellido': apellido,
        'username': username,
        'email': email,
        'contrasenia': contrasenia,
        }
        lista_usuarios.append(self.nuevo_usuario)
        print(self.nuevo_usuario)
        return self.nuevo_usuario
 """

persona1 = Usuario(1,"Maria","Martin","Mary","mary@gmail.com","HDVLM","12/05/2023",False)
persona1.login()