from data.install import *
os.chdir('/data/data/com.termux/files/usr/etc/')
usr = os.path.exists('.usuario')
install()


try:
    while True:
        from time import sleep
        from data.menu import *
        from data.ferramentas import clear
        clear()
        if not usr:
            print(f'{cy}~Lursy: {vd}Olá tudo bem ?...')
            sleep(1)
            print('        É sua primeira vez por aqui?')
            sleep(3.5)
            clear()
            print(f'{cy}~Lursy: {vd}Bem vamos lá ... ')
            sleep(1)
            print('        Seja bem vindo!!')
            sleep(2)
            print('        Esse é o menu, fique a vontade ok :D')
            sleep(1.4)
        print(--JeehVQV--)
        user = (open('.usuario', 'r')).readline()
        print(f'''{ve}┏━━━━━━━━━━━━━━━━━┓
  {am}[ 1 ] {br}-{cy} escolha uma letra
  {am}[ 2 ] {br}-{cy} escolha um banner
  {am}[ 3 ] {br}-{cy} escolha uma senha
  {am}[ 4 ] {br}-{cy} {user}
  {am}[ 5 ] {br}-{cy} Sair
{ve}┗━━━━━━━━━━━━━━━━━┛
''')
        menu = str(input(f'{am}//: {br}'))
        if usr == False:
            print(f'{cy}~Lursy: {vd}Boa escolha garoto(a)!')
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
            print(f'\n{vd}Saindo aqui , fuii ...')
            sleep(1)
            clear()
            break
        else:
            print(f'{ve}Comando não reconhecido')
            sleep(1)
except KeyboardInterrupt:
    print(f'\n{vd}Saindo...')
    sleep(1)
    clear()
