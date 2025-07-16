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
    nom_marca = input('Ingrese marca a consultar: ').strip().capitalize()
    encontrados = []
    for codigo, datos in productos.items():
        if datos[0] == nom_marca:
            encontrados.append((codigo, stock.get(codigo, ['Sin precio', 0])[1]))
    if encontrados:
        print(f'Stock para la marca {nom_marca}:')
        for codigo, cantidad in encontrados:
            print(f'Código: {codigo} - Stock: {cantidad}')
    else:
        print(f'No se encontraron notebooks de la marca {nom_marca}.')

def busqueda_precio():
    try:
        p_min = int(input('Ingrese precio mínimo: '))
        p_max = int(input('Ingrese precio máximo: '))
    except ValueError:
        print('Debe ingresar valores numéricos.')
        return
    encontrados = []
    for codigo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            encontrados.append((codigo, precio, cantidad))
    if encontrados:
        print('Notebooks en el rango de precio:')
        for codigo, precio, cantidad in encontrados:
            print(f'Código: {codigo} - Precio: {precio} - Stock: {cantidad}')
    else:
        print('No hay notebooks en ese rango de precio.')

def list_prod():
    print('-------- Listado de Notebooks Ordenados --------')
    print(productos)

#Modificación 1

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