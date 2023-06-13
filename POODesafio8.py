#atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado, online
# métodos: login(), registrar()


#objeto = persona
#usuario = clase, el molde

class Usuario:
    def __init__(self,username,contrasenia,estado=False):
      self.username = 'Tatiana'
      self.contrasenia = '123456'
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
    
    
    def iniciar_sesion(self):
        ingresar_contrasenia = input("Ingrese su contraseña: ")      
        if ingresar_contrasenia == self.contrasenia:
          print("Contraseña correcta.") 
          self.estado = True
        else:
           print("Contraseña incorrecta. Intente de nuevo.")

usuario1 = Usuario(input("Ingrese su nombre de usuario: "), input("Ingrese su contraseña: ")) 
usuario1.iniciar_sesion()