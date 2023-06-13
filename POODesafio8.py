#atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado
# métodos: login(), registrar()


#objeto = persona
#usuario = clase, el molde

class Usuario:
    def __init__(self,id,nombre,apellido,username,email,contrasenia,fecha_registro,estado=False):
      self.id = id
      self.nombre = nombre
      self.apellido = apellido
      self.username = username
      self.email = email
      self.contrasenia = contrasenia
      self.fecha_registro = fecha_registro
      self.estado = estado
      
    

    def get_user(self):
       return self.username


    def get_contrasenia(self):
       return self.contrasenia

    def __str__(self):
      if self.estado:
          conectado = "conectado"
      else: 
          conectado = "desconectado" 
      return f"El nombre de usuario es {self.username} y está {conectado}"
    
    
    def login(self):
        ingresar_contrasenia = input("Ingrese su contraseña: ")      
        if ingresar_contrasenia == self.contrasenia:
          print("Contraseña correcta.") 
          self.estado = True
        else:
           print("Contraseña incorrecta. Intente de nuevo.")

    def registrar(self):
        nombre = input("Ingrese su nombre: ")
        username = input("Ingrese su username: ") 
        contrasenia = input("Ingrese su contrasenia: ")



usuario1 = Usuario(input("Ingrese su nombre de usuario: "), input("Ingrese su contraseña: ")) 
usuario1.login()