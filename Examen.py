productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}

def stock_marca():
    while True:
        nom_marca = input('Ingrese marca a consultar: ')
        print(f'El stock es: {stock}')
        return

def busqueda_precio():
    p_min = int(input('Ingrese precio mínimo: '))
    p_max = int(input('Ingrese precio máximo: '))
    if p_min >= 900000 and p_max >= 1200000:
        print('No hay notebooks en ese rango de precio.')
    print(f'Los notebooks entre los precios consultas son: {stock}')

def list_prod():
    print('-------- Listado de Notebooks Ordenados --------')
    print(productos)

def termino():
    print('Programa finalizado')
    print('Hasta luego!')  # Pequeño arreglo: mensaje de despedida

while True:
    print('MENÚ PRINCIPAL')
    print('====================================')
    print('1. Stock Marca')
    print('2. Busqueda por precio')
    print('3. Listado de productos.')
    print('4. Salir.')
    opc = input('Ingrese Opción: ')
    if opc == '1':
        stock_marca()
    elif opc == '2':
        busqueda_precio()
    elif opc == '3':
        list_prod()
    elif opc == '4':
        termino()
        break
    else:
        print('Opción Incorrecta')
#ola profe soy el sebastian sellao ise todo