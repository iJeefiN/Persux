from data.install import *
os.chdir('/data/data/com.termux/files/usr/etc/')
usr = os.path.exists('.usuario')
install()
from time import sleep
from data.menu import *


try:
    while True:
        os.system('clear')
        if usr == False:
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
        user = (open('.usuario', 'r')).readline()
        print(f'''{ve}┏━━━━━━━━━━━━━━━━━┓
  {am}[ 1 ] {br}-{cy} letra
  {am}[ 2 ] {br}-{cy} banner
  {am}[ 3 ] {br}-{cy} senha
  {am}[ 4 ] {br}-{cy} {user}
  {am}[ 5 ] {br}-{cy} Sair
{ve}┗━━━━━━━━━━━━━━━━━┛
''')
        menu = str(input(f'{am}//: {br}'))
        if usr == False and menu != '5':
            print(f'{cy}~Lursy: {vd}Boa escolha!')
            sleep(1)
            usr = True
        if menu == '1':
            from data.letra import letra
            letra()
        elif menu == '2':
            from data.banner import banner
            banner()
        elif menu == '3':
            from data.senha import senha
            senha()
        elif menu == '4':
            from data.nome import nome_letra
            nome_letra()
            from data.ferramentas import *
        elif menu == '5':
            print(f'\n{vd}Saindo...')
            sleep(1)
            os.system('clear')
            break
        else:
            print(f'{ve}Comando não reconhecido')
            sleep(1)
except KeyboardInterrupt:
    print(f'\n{vd}Saindo...')
    sleep(1)
    os.system('clear')
