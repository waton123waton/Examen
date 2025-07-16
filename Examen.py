class NotebookStore:
    def __init__(self):
        self.productos = {
            '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
        }
        self.stock = {
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

    def stock_marca(self):
        nom_marca = input('Ingrese marca a consultar: ').strip().capitalize()
        encontrados = []
        for codigo, datos in self.productos.items():
            if datos[0] == nom_marca:
                encontrados.append((codigo, self.stock.get(codigo, ['Sin precio', 0])[1]))
        if encontrados:
            print(f'Stock para la marca {nom_marca}:')
            for codigo, cantidad in encontrados:
                print(f'Código: {codigo} - Stock: {cantidad}')
        else:
            print(f'No se encontraron notebooks de la marca {nom_marca}.')

    def busqueda_precio(self):
        try:
            p_min = int(input('Ingrese precio mínimo: '))
            p_max = int(input('Ingrese precio máximo: '))
        except ValueError:
            print('Debe ingresar valores numéricos.')
            return
        encontrados = []
        for codigo, (precio, cantidad) in self.stock.items():
            if p_min <= precio <= p_max and cantidad > 0:
                encontrados.append((codigo, precio, cantidad))
        if encontrados:
            print('Notebooks en el rango de precio:')
            for codigo, precio, cantidad in encontrados:
                print(f'Código: {codigo} - Precio: {precio} - Stock: {cantidad}')
        else:
            print('No hay notebooks en ese rango de precio.')

    def list_prod(self):
        print('-------- Listado de Notebooks Ordenados --------')
        productos_con_precio = []
        for codigo, datos in self.productos.items():
            precio = self.stock.get(codigo, [None])[0]
            if precio is not None:
                productos_con_precio.append((codigo, datos, precio))
        productos_con_precio.sort(key=lambda x: x[2])
        for codigo, datos, precio in productos_con_precio:
            print(f'Código: {codigo} | Marca: {datos[0]} | Pantalla: {datos[1]}" | RAM: {datos[2]} | Disco: {datos[3]} {datos[4]} | Procesador: {datos[5]} | Video: {datos[6]} | Precio: {precio}')

    def salir(self):
        print('Programa finalizado')
        print('Hasta luego!')

    def menu(self):
        while True:
            print('\nMENÚ PRINCIPAL')
            print('====================================')
            print('1. Stock Marca')
            print('2. Busqueda por precio')
            print('3. Listado de productos.')
            print('4. Salir.')
            opc = input('Ingrese Opción: ').strip()
            if opc == '1':
                self.stock_marca()
            elif opc == '2':
                self.busqueda_precio()
            elif opc == '3':
                self.list_prod()
            elif opc == '4':
                self.salir()
                break
            else:
                print('Opción Incorrecta')

if __name__ == "__main__":
    tienda = NotebookStore()
    tienda.menu()