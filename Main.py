import Calculadora

# TODO: Aplicar Try-Except
#       Aplicar estructuras de control

def main():
    
    print("Calculadora básica")
    calc = Calculadora.Calculadora()
    print ("Valor inicial:")
    calc.entrada = int(input())
    calc.suma() 
    print(calc.aux)
    print ("Valor para sumar:")
    calc.entrada = int(input())
    calc.sumar()
    calc.mostrar_resultado()
    print(calc.resultado)


if __name__ == "__main__":
    main()