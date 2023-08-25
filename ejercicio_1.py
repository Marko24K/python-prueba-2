def main():
    def primo(n):
        i = 2
        for i in range (n-1):
            if(n%i != 0):
                return True
            else:
                return False
            
    numero = primo (5)
    if(numero == True):
        print("es primo")
    if(numero == False):
        print("no es primo")
        


if __name__ == '__main__':
    main()
