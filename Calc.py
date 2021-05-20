
#bin/bash/python3
#Calc by ©®1pto9
import os
import math
import sys

#colores
v = "\033[1;32m"
cy = "\033[1;36m"
r = "\033[1;31m"
b = "\033[1;37m"
a = "\033[1;33m"
m = "\033[1;35m"

os.system('clear')

def menu():
        menu = '''



        ***,*,*,(%&&&%&%@,,...........
*/&(*%/#@@@@&#((#&@..................
*/#&(##@#**,%&&&*%@&%.,**,,,,.......
***(&&@@&#%%(&@&%%%%@%%,............
,,**/#@/&@&%(/@@@%%#%&@#%...*,......
,,,,,*/&&@*&&%%%&.&&%/##@&%* .......
,,,,,,,/(@*/&%@@@%%/#&&&@&(.........'''

        print(menu)
        print(f'{v}\tMenu \n{r}[1]Suma: \n{m}[2]Resta: \n{b}[3]Multiplicacion \n{a}[4]Division \n[5]{v}Potencia: \n{r}[6]Raiz Cuadrada \n{b}[7]Salir:')

while True:
        try:
                menu()
                opcion = int(input(f'{a}Ingrese opcion ==>\n '))
                if opcion == 1:
                        p1 = int(input(f'{a}Ingrese primer numero ==>{b}\n'))
                        p2 = int(input(f'{a}Ingrese segundo numero ==>{b}\n'))
                        resultado = p1 + p2
                        print(f'{a}El resultado de la suma es:{r} {resultado}')
                        i = input(f'{cy}presione enter para continuar ')
                        os.system('clear')
                elif opcion == 2:
                #   menu()
                        n1 = int(input(f'{a}Ingrese primer numero ==>\n '))
                        n2 = int(input(f'{a}Ingrese segundo numero ==>\n '))
                        resultado = n1 - n2
                        print(f'El resultado es:{r} {resultado}')
                        l = input(f'{cy}Enter para continuar ')
                        os.sytem('clear')
                elif opcion == 3:
                #   menu()
                        n1 = int(input(f'{a}Ingrese primer numero ==>\n'))
                        n2 = int(input(f'{a}Ingrese segundo numero ==>\n'))
                        resultado = n1 * n2
                        print(f'El resultado de la multiplicacion es:{r} {resultado}')
                        l = input(f'{cy}Enter para continuar')
                        os.system('clear')
                elif opcion == 4:
                #   menu()
                        n1 = int(input(f'{a}Ingrese primer numero ==>\n'))
                        n2 = int(input(f'{a}Ingrese segundo numero ==>\n'))
                        resultado =  n1/n2
                        print(f'El resultado de la divison es: {r} {resultado}')
                        l = input(f'{cy}Enter para continuar')
                        os.system('clear')
                elif opcion == 5:
                #   menu()
                        n1 = int(input(f'{a}Ingrese primer numero ==>{b}\n'))
                        n2 = int(input(f'{a}Ingrese segundo numero ==>{b}\n'))
                        print(f'{b}El resultado de la potencia es: {red}')
                        print(pow(n1, n2))
                        l = input(f'{cy} Enter para continuar ')
                        os.system('clear')
                elif opcion == 6:
                #       menu()
                        n1 = int(input(f'{a}Ingrese  numero a sacar raiz ==>{b}\n'))
                        resultado = math.sqrt(n1)
                        print(f'El resultado de la raiz es: {red} {resultado}')
                        l = input(f'{cy}Enter para continuar ')
                        os.system('clear')
                elif opcion == 7:
                        menu()
                        sys.exit()

                else:
                        print(f'{cy}Opcion no registrada')
        except Exception as e:
                print(e)
