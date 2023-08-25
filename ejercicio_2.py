def main():
    opcion = int(input("""
                       Escoja una opcion:
                       0)salir
                       1) Kilometros a Millas
                       2) Millas a Kilometros
                       3) kilogramos a libras
                       4) libras a kilogramos
                       5) Celsius a Fahrenheit
                       6) Fahrenheit a Celsius
                       """))
    while(opcion != 0):
        if(opcion == 1):
            unidad = float(input("Ingrese la unidad a convertir en Kilometros: "))
            conversion = unidad * 0.62137
            print(f"Su valor convertido es: {conversion}")

        elif(opcion == 2):
            unidad = float(input("Ingrese la unidad a convertir en Millas: "))
            conversion = unidad *1.6093
            print(f"Su valor convertido es: {conversion}")

        elif(opcion == 3):
            unidad = float(input("Ingrese la unidad a convertir en kilogramos: "))
            conversion = unidad * 2.2046
            print(f"Su valor convertido es: {conversion}")

        elif(opcion == 4):
            unidad = float(input("Ingrese la unidad a convertir en libras: "))
            conversion = 0.453592
            print(f"Su valor convertido es: {conversion}")
        elif(opcion == 5):
            unidad = float(input("Ingrese la unidad a convertir en Celsius: "))
            conversion = (unidad * 9/5) + 32
            print(f"Su valor convertido es: {conversion}")

        elif(opcion == 6):
            unidad = float(input("Ingrese la unidad a convertir en  Fahrenheit: "))
            conversion = (unidad - 32) * 5/9
            print(f"Su valor convertido es: {conversion}")
    print("Que tenga buen dia :)")

if __name__ == '__main__':
    main()