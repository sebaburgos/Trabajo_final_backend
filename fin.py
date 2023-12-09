stock_mouse = {
    "M001": {
        "tipo": "mouse",
        "marca": "logitech",
        "modelo": "m 100 usb",
        "precio": 2000,
        "stock_actual": 10,
    },
    "M002": {
        "tipo": "mouse",
        "marca": "acer predator",
        "modelo": "cestus 500 gamer",
        "precio": 3000,
        "stock_actual": 15,
    },
}
stock_teclado = {
    "TC01": {
        "tipo": "teclado",
        "marca": "maxell",
        "modelo": "KB-90",
        "precio": 9000,
        "stock_actual": 5,
    },
    "TC02": {
        "tipo": "teclado",
        "marca": "lenovo",
        "modelo": "G 470",
        "precio": 5000,
        "stock_actual": 4,
    },
}
stock_monitor = {
    "MN01": {
        "tipo": "monitor",
        "marca": "noblex",
        "modelo": "LFT2534",
        "precio": 45000,
        "stock_actual": 3,
    },
    "MN02": {
        "tipo": "monitor",
        "marca": "samsung",
        "modelo": "sm5785",
        "precio": 75000,
        "stock_actual": 5,
    },
}
stock = {
    "mouse": stock_mouse,
    "teclado": stock_teclado,
    "monitor": stock_monitor,
}

usuario = "admin"
password = "1234"

print("Bienvenido a nuestra tienda")
print()

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
    print(
        "Usted ha superado el limite de intentos de login. "
    )  

def menu_principal():
    while True:
        print("MENU PRINCIPAL:")
        print("Seleccione una opción:")
        print("1. GESTION DE PRODUCTOS")
        print("2. INFORMES")
        print("3. CERRAR SESION")
        opcion = input()
        while (
            opcion != "1" and opcion != "2" and opcion != "3"
        ):  
            opcion = input("Opción no válida. Reingrese:")
        match opcion:
            case "1":
                print("Elegiste gestion de productos")
                gestion_productos()
            case "2":
                print("Elegiste informes")
                menu_informes()
            case "3":
                print("Elegiste cerrar sesión.\nHasta pronto")
                break


def gestion_productos():
    print("MENU GESTION DE PRODUCTOS")
    opciones = [
        "1",
        "2",
        "3",
        "4",
    ]  
    opcion = None
    while opcion not in opciones:
        print("Que desea realizar? ")
        print("1. INGRESAR PRODUCTO AL STOCK: ")
        print("2. MODIFICAR PRODUCTO EXISTENTE")
        print("3. ELIMINAR UN PRODUCTO")
        print("4. VOLVER AL MENU PRINCIPAL")
        opcion = (
            input()
        )  
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
    print("3.Mostrtar las caracteristicas de un producto")
    opcion = input()
    if opcion == "1":
        mostrar_stock_completo()
    elif opcion == "2":
        mostrar_produc_por_categoria()
    elif opcion == "3":
        mostrar_por_codigo()
    else:
        print("Opcion no valida. Reintente")


def modificar_prod_existente():
    categoria = None
    
    print("Las categorías existentes son:")
    for i in stock:
        print(i)

    while categoria not in stock:
        categoria = input("Ingrese la categoría a modificar: ").lower()
        if categoria not in stock:
            print("Categoría inexistente, reintente.")

    print(f"Los códigos de productos en la categoría {categoria} son:")
    for j in stock[categoria]:
        print(j)

    codigo = input("Ingrese el código del producto a modificar: ").upper()

    while codigo not in stock[categoria]:
        print("Código inexistente. Por favor, ingrese un código válido.")
        codigo = input("Ingrese el código del producto a modificar: ").upper()

    print("Atributos actuales del producto:")
    for atributo, valor in stock[categoria][codigo].items():
        print(f"{atributo}: {valor}")

    while True:
        atributo = input(
            "¿Qué atributo desea modificar? \nO ingrese salir para finalizar: "
        )

        if atributo == "salir":
            break

        if atributo not in stock[categoria][codigo]:
            print("Atributo no válido. Intente nuevamente.")
            continue

        if atributo == "marca" or atributo == "tipo" or atributo == "modelo":
            valor = input(f"Ingrese el nuevo valor de {atributo}: ")
        else:
            valor = float(input(f"Ingrese el nuevo valor de {atributo}: "))

        stock[categoria][codigo][atributo] = valor

    print("Atributos actualizados del producto:")
    for atributo, valor in stock[categoria][codigo].items():
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
            for categoria in stock:
                print(categoria)
            categoria = input("Ingrese la categoría del producto: ")

            while categoria not in stock:
                print("Categoría no válida. Vuelva a intentar.")
                categoria = input("Ingrese la categoría del producto: ")
        else:
            categoria = input("Ingrese la nueva categoría: ")
            stock[categoria] = {}

        codigo = input("Ingrese el código del producto: ")
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        precio = float(input("Ingrese el precio: "))
        stock_actual = int(input("Ingrese la cantidad: "))
        stock[categoria][codigo] = {
            "precio": precio,
            "marca": marca,
            "modelo": modelo,
            "stock_actual": stock_actual,
        }

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
        encontrado = False
        
        for categoria, productos in stock.items():
            
            if codigo in productos:
                del productos[codigo]
                encontrado = True
            
                print(f"{codigo} ha sido eliminado.")
                break
            
        if not encontrado:
            print("CÓDIGO NO VÁLIDO.")
            print("Los códigos existentes son:")
            for categoria, productos in stock.items():
                print(f"{categoria}:")
                for clave in productos.keys():
                    print(clave)

        respuesta = input("¿Desea eliminar otro producto? (s/n)").lower()
        while respuesta != "s" and respuesta != "n":
            respuesta = input(
                "Entrada no válida. ¿Desea eliminar otro producto? (s/n)"
            ).lower()

        if respuesta == "n":
            break

    

def mostrar_stock_completo():
    for categoria, productos in stock.items():
        
        print(categoria.upper())
        
        for codigo, atributos in productos.items():
            print(len(categoria) * " ", codigo)
            
            for descripcion, valor in atributos.items():
                print(len(categoria + codigo) * " ", descripcion, ":", valor)

def mostrar_produc_por_categoria():
    continuar = "s"
    while continuar == "s":
        categoria = input("¿De qué categoría desea obtener el informe?: ")
        while categoria not in stock:
            print("CATEGORÍA INEXISTENTE. Las categorías existentes son:")
            for i in stock:
                print(i)
            categoria = input("Ingrese una categoría válida:\n")
        print("INFORME DE CATEGORÍA", categoria)
        for codigo, atributos in stock[categoria].items():
            print(codigo)
            for descripcion, valor in atributos.items():
                print(len(codigo) * " ", descripcion, ":", valor)
        continuar = input("¿Desea obtener el informe de otra categoría? (s/n)").lower()
        while continuar != "s" and continuar != "n":
            continuar = input("DATO NO VÁLIDO. ¿Desea obtener el informe de otra categoría? (s/n)").lower()

def mostrar_por_codigo():
    print("INFORME DE PRODUCTO")
    continuar = "s"
    while continuar == "s":
        codigo = input("Ingrese el código del producto: ").upper()
        encontrado = False
        while not encontrado:
            for categoria in stock:
                if codigo in stock[categoria]:
                    encontrado = True
                    break
            if not encontrado:
                codigo = input("CÓDIGO INEXISTENTE. Reingrese el código: ").upper()
        print("Las características del producto", codigo,"son: ")
        for categoria in stock:
            if codigo in stock[categoria]:
                for atributo, valor in stock[categoria][codigo].items():
                    print(atributo, ":", valor)
                break
        continuar = input("¿Desea ver otro producto? (s/n): ").lower()
        while continuar != "s" and continuar != "n":
            continuar = input("Dato invalido. ¿Desea ver otro producto? (s/n): ").lower()


if login():

 menu_principal()
