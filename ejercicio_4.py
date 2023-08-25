def main():
    compra = {}
    opcion = int(input("""
                       opcion 0 (salir)
                       opcion 1 (comprar)"""))
    while(opcion != 0):
        articulo = input("Ingrese el producto: ")
        precio = input("precio: ")
        compra[articulo] = precio
        opcion = int(input("""
            opcion 0 (salir)
            opcion 1 (comprar)"""))
        
    
    print("lista de la compra")

if __name__ == '__main__':
    main()