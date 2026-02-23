class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
    def agregar_amigo(self, otro_usuario):
        if otro_usuario not in self.amigos:
            self.amigos.append(otro_usuario)
            print(f" {otro_usuario.nombre} ahora es amigo de {self.nombre}")
        else:
            print("ya son amigos.")
    def mostrar_amigos(self):
        if not self.amigos:
            print(f"{self.nombre} no tiene amigos agregados.")
        else:
            print(f"\n amigos de {self.nombre}:")
            for i, amigo in enumerate(self.amigos, start=1):
                print(f"{i}. {amigo.nombre}")
        print()
class RedSocial:
    def __init__(self):
        self.usuarios = []
    def crear_usuario(self, nombre):
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        print("usuario creado correctamente.\n")
    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None
    def agregar_amistad(self, nombre1, nombre2):
        usuario1 = self.buscar_usuario(nombre1)
        usuario2 = self.buscar_usuario(nombre2)
        if usuario1 and usuario2:
            usuario1.agregar_amigo(usuario2)
            usuario2.agregar_amigo(usuario1)
            print("smistad agregada correctamente.\n")
        else:
            print("uno o ambos usuarios no existen.\n")
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("no hay usuarios registrados.\n")
        else:
            print("\n usuarios registrados:")
            for i, usuario in enumerate(self.usuarios, start=1):
                print(f"{i}. {usuario.nombre}")
            print()
def menu():
    red = RedSocial()
    while True:
        print("redes social basico")
        print("1. crear usuario")
        print("2. agregar amistad")
        print("3. mostrar usuarios")
        print("4. mostrar amigos de un usuario")
        print("5. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            nombre = input("ingrese nombre del usuario: ")
            red.crear_usuario(nombre)
        elif opcion == "2":
            nombre1 = input("ingrese nombre del primer usuario: ")
            nombre2 = input("ingrese nombre del segundo usuario: ")
            red.agregar_amistad(nombre1, nombre2)
        elif opcion == "3":
            red.mostrar_usuarios()
        elif opcion == "4":
            nombre = input("ingrese nombre del usuario: ")
            usuario = red.buscar_usuario(nombre)
            if usuario:
                usuario.mostrar_amigos()
            else:
                print("usuario no encontrado.\n")
        elif opcion == "5":
            print("saliendo de la red social...")
            break
        else:
            print("opcion invalida.\n")
menu()