from data.install import *
from data.menu import *


install()
nms = 2


try:
    while True:
            if nms != 1:
                print(persuxf)
                print(menu_inicial)
            else:
                print(f'{cy}~Lursy: {vd}Olá...')
                sleep(1)
                print('        É sua primeira vez por aqui?')
                sleep(3.5)
                os.system('clear')
                print(f'{cy}~Lursy: {vd}Bem... ')
                sleep(1)
                print('        Seja bem vindo!!')
                sleep(2)
                print('        Esse é o menu, fique a vontade :D')
                sleep(1.4)
                print(persuxf)
                print(menu_inicial)
            menu = int(input(f'{am}//: {br}'))
            if nms == 1 and menu < 4:
                print(f'{cy}~Lursy: {vd}Boa escolha!')
                sleep(1)
                nms = 3
            if menu == 1:
                from data.letra import *
                letra()
            elif menu == 2:
                from data.banner import *
                banner()
            elif menu == 3:
                from data.senha import *
                senha()
            elif menu == 4:
                print(f'\n{vd}Saindo...')
                sleep(1)
                break
            else:
                print(f'{ve}Comando não reconhecido')
                sleep(1)
            os.system('clear')
except KeyboardInterrupt:
    print(f'\n{vd}Saindo...')
    sleep(1)
    os.system('clear')
