def main():
    compra = {}
    opcion = int(input("""
                       opcion 0 (salir)
                       opcion 1 (comprar)
                       """))
    while(opcion != 0):
        articulo = input("Ingrese el producto: ")
        compra[articulo] = float(input("precio: "))
        opcion = int(input("""
            opcion 0 (salir)
            opcion 1 (comprar)"""))
        
    
    print("lista de la compra")
    print("----------------------")
    total = 0
    for i in compra:
        print(f"{i}     {compra[i]}")
        total += compra[articulo]
    print (f"Total:   {total}")
if __name__ == '__main__':
    main()