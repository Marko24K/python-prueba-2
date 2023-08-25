def main():
    def palindromo(palabra):
        palabra = palabra.replace(" ","")
        palabra = palabra.lower()
        inversa = palabra[::-1]
        if(palabra == inversa):
            return True
        else:
            return False
    palabra = str(input("ingrese una palabra: "))
    n=palindromo(palabra)
    if(n == True):
        print("es palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    main()
