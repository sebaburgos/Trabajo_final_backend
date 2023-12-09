class Producto:
    def _init_(self, tipo, marca, modelo, precio, stock_actual):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.stock_actual = stock_actual


class Stock:
    def _init_(self):
        self.stock = {}

    def agregar_producto(self, categoria, codigo, producto):
        if categoria not in self.stock:
            self.stock[categoria] = {}
        self.stock[categoria][codigo] = producto

    def eliminar_producto(self, codigo):
        for categoria, productos in self.stock.items():
            if codigo in productos:
                del productos[codigo]
                print(f"{codigo} ha sido eliminado.")
                return
        print("CÓDIGO NO VÁLIDO.")

    def mostrar_stock_completo(self):
        for categoria, productos in self.stock.items():
            print(categoria.upper())
            for codigo, producto in productos.items():
                print(len(categoria) * " ", codigo)
                for atributo, valor in producto._dict_.items():
                    print(len(categoria + codigo) * " ", atributo, ":", valor)

    def mostrar_produc_por_categoria(self, categoria):
        if categoria not in self.stock:
            print("CATEGORÍA INEXISTENTE.")
            return

        print("INFORME DE CATEGORÍA", categoria)
        for codigo, producto in self.stock[categoria].items():
            print(codigo)
            for atributo, valor in producto._dict_.items():
                print(len(codigo) * " ", atributo, ":", valor)

    def mostrar_por_codigo(self, codigo):
        encontrado = False
        for categoria in self.stock:
            if codigo in self.stock[categoria]:
                encontrado = True
                print("Las características del producto", codigo, "son:")
                for atributo, valor in self.stock[categoria][codigo]._dict_.items():
                    print(atributo, ":", valor)
                break

        if not encontrado:
            print("CÓDIGO INEXISTENTE.")


stock = Stock()  # Instancia de la clase Stock

usuario = "admin"
password = "1234"


def login():
    for i in range(3):
        user = input("Ingrese el nombre de usuario: ")
        if usuario == user.lower():
            for j in range(3):
                contrasenia = input("Ingrese la contraseña: ")
                if password == contrasenia:
                    print("Bienvenido a tecno house")
                    return True
                else:
                    print("Error al ingresar")
            break
        else:
            print("Error de usuario")
    print("Usted ha superado el límite de intentos de login.")


def menu_principal():
    while True:
        print("MENU PRINCIPAL:")
        print("Seleccione una opción:")
        print("1. GESTION DE PRODUCTOS")
        print("2. INFORMES")
        print("3. CERRAR SESIÓN")
        opcion = input()
        while opcion not in ["1", "2", "3"]:
            opcion = input("Opción no válida. Reingrese:")
        if opcion == "1":
            print("Elegiste gestion de productos")
            gestion_productos()
        elif opcion == "2":
            print("Elegiste informes")
            menu_informes()
        elif opcion == "3":
            print("Elegiste cerrar sesión.\nHasta pronto")
            break


def gestion_productos():
    print("MENU GESTION DE PRODUCTOS")
    opciones = ["1", "2", "3", "4"]
    opcion = None
    while opcion not in opciones:
        print("Que desea realizar? ")
        print("1. INGRESAR PRODUCTO AL STOCK: ")
        print("2. MODIFICAR PRODUCTO EXISTENTE")
        print("3. ELIMINAR UN PRODUCTO")
        print("4. VOLVER AL MENU PRINCIPAL")
        opcion = input()
        if opcion not in opciones:
            print("OPCION NO VALIDA.")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        modificar_prod_existente()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        menu_principal()


def menu_informes():
    print("Bienvenido al menu informes")
    print("¿Que desea realizar?")
    print("1.Mostrar el stock completo")
    print("2.Mostrar productos por categoria")
    print("3.Mostrar las caracteristicas de un producto")
    opcion = input()
    if opcion == "1":
        stock.mostrar_stock_completo()
    elif opcion == "2":
        categoria = input("Ingrese la categoría: ")
        stock.mostrar_produc_por_categoria(categoria)
    elif opcion == "3":
        codigo = input("Ingrese el código del producto: ")
        stock.mostrar_por_codigo(codigo)
    else:
        print("Opcion no valida. Reintente")


def modificar_prod_existente():
    categoria = None

    print("Las categorías existentes son:")
    for i in stock.stock:
        print(i)

    while categoria not in stock.stock:
        categoria = input("Ingrese la categoría a modificar: ").lower()
        if categoria not in stock.stock:
            print("Categoría inexistente, reintente.")

    print(f"Los códigos de productos en la categoría {categoria} son:")
    for j in stock.stock[categoria]:
        print(j)

    codigo = input("Ingrese el código del producto a modificar: ").upper()

    while codigo not in stock.stock[categoria]:
        print("Código inexistente. Por favor, ingrese un código válido.")
        codigo = input("Ingrese el código del producto a modificar: ").upper()

    print("Atributos actuales del producto:")
    for atributo, valor in stock.stock[categoria][codigo]._dict_.items():
        print(f"{atributo}: {valor}")

    while True:
        atributo = input(
            "¿Qué atributo desea modificar? \nO ingrese salir para finalizar: "
        )

        if atributo == "salir":
            break

        if atributo not in stock.stock[categoria][codigo]._dict_:
            print("Atributo no válido. Intente nuevamente.")
            continue

        if atributo == "marca" or atributo == "tipo" or atributo == "modelo":
            valor = input(f"Ingrese el nuevo valor de {atributo}: ")
        else:
            valor = float(input(f"Ingrese el nuevo valor de {atributo}: "))

        setattr(stock.stock[categoria][codigo], atributo, valor)

    print("Atributos actualizados del producto:")
    for atributo, valor in stock.stock[categoria][codigo]._dict_.items():
        print(f"{atributo}: {valor}")


def agregar_producto():
    while True:
        print("¿Qué desea realizar?")
        print("1. Agregar un producto perteneciente a una categoría existente.")
        print("2. Agregar un producto perteneciente a una nueva categoría.")
        opcion = input()

        while opcion != "1" and opcion != "2":
            opcion = input("Opción incorrecta. Vuelva a intentar: ")

        if opcion == "1":
            print("Categorías disponibles:")
            for categoria in stock.stock:
                print(categoria)
            categoria = input("Ingrese la categoría del producto: ")

            while categoria not in stock.stock:
                print("Categoría no válida. Vuelva a intentar.")
                categoria = input("Ingrese la categoría del producto: ")
        else:
            categoria = input("Ingrese la nueva categoría: ")
            stock.stock[categoria] = {}

        codigo = input("Ingrese el código del producto: ")
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        precio = float(input("Ingrese el precio: "))
        stock_actual = int(input("Ingrese la cantidad: "))
        producto = Producto(tipo=categoria, marca=marca, modelo=modelo, precio=precio, stock_actual=stock_actual)
        stock.agregar_producto(categoria, codigo, producto)

        continuar = input("¿Desea continuar agregando productos? (s/n)").lower()

        while continuar != "s" and continuar != "n":
            continuar = input(
                "Dato no válido. ¿Desea continuar agregando productos? (s/n)"
            ).lower()

        if continuar == "n":
            break


def eliminar_producto():
    while True:
        codigo = input("Ingrese el codigo del producto a eliminar: ").upper()
        stock.eliminar_producto(codigo)

        respuesta = input("¿Desea eliminar otro producto? (s/n)").lower()
        while respuesta != "s" and respuesta != "n":
            respuesta = input(
                "Entrada no válida. ¿Desea eliminar otro producto? (s/n)"
            ).lower()

        if respuesta == "n":
            break


if login():
    menu_principal()