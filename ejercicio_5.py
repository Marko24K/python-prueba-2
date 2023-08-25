def main():
    palabra = str(input("ingrese una palabra: "))
    letra = str(input("ingrese una letra: "))
    c = 0
    for i in palabra:
        if (letra == i):
            c+=1
    print(f"En la palabra {palabra} la letra {letra} aparece {c} veces")

if __name__ == '__main__':
    main()