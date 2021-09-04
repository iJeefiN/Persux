from data.ferramentas import *
from data.menu import bannerf, menu_cores, ban_sen, styles


def banner():
    while True:
        rsenha = ''
        rcor = open('.Cor', 'r')
        vs = os.path.exists('.Senha')
        vn = os.path.exists('.Nick')
        if vs:
            rsenha = open('.Senha', 'r')
        if vn:
            print(ban_sen)
            ban_exists = str(input(f'{am}//: {br}'))
            if ban_exists == '1':
                os.system('clear')
                pass
            elif ban_exists == '2':
                os.system('rm -rf .Nick')
                os.system('rm -rf bash.bashrc')
                bash = open('bash.bashrc', 'w')
                bash.write(f'{inicio}\n' + f'\n{rsenha.read()}\n{rcor.read()}' if vs
                           else f'{rcor.read()}' + f'{final}')
                bash.close()
                print(f'{vd}!Sucess!')
                sleep(1)
                break
            elif ban_exists == '3':
                os.system('clear')
                break
            else:
                print(f'{ve}{ban_exists} não é um comando')
                sleep(2)
                break
        os.system('clear')
        print(bannerf)
        name = nick = str(input(f'{am}Nick: {br}'))
        os.system('clear')
        print(f"{rx}{figlet.renderText('Styles')}")
        print(styles)
        int_styles = str(input(f'{am}//: {br}'))
        if int_styles == '1':
            banner_nick = f'''echo -e '\e[0;:corm'
figlet {nick}
echo -e '\e[m\\n' '''
        elif int_styles == '2':
            name = poison.renderText(f'{nick}')
        elif int_styles == '3':
            name = lean.renderText(f'{nick}')
        elif int_styles == '4':
            name = block.renderText(f'{nick}')
        elif int_styles == '5':
            name = alligator.renderText(f'{nick}')
        else:
            print(f'{ve}Comando não identificado!')
            sleep(2)
            break
        if int_styles != '1':
            banner_nick = f'''echo -e '\e[0;:corm'
echo """{name}"""
echo -e '\e[m\\n' '''
        os.system('clear')
        nick_banner = banner_nick.replace(':name', f'{nick}')
        os.system('clear')
        print(f"{az}{figlet.renderText('Cores')}")
        print(menu_cores)
        cor_name = str(input(f'\n{am}//: {br}'))
        os.chdir('/data/data/com.termux/files/usr/etc')
        os.system('rm -rf bash.bashrc')
        if cor_name == '1':
            snick = nick_banner.replace(':cor', '31')
        elif cor_name == '2':
            snick = nick_banner.replace(':cor', '33')
        elif cor_name == '3':
            snick = nick_banner.replace(':cor', '37')
        elif cor_name == '4':
            snick = nick_banner.replace(':cor', '32')
        elif cor_name == '5':
            snick = nick_banner.replace(':cor', '36')
        elif cor_name == '6':
            snick = nick_banner.replace(':cor', '34')
        elif cor_name == '7':
            snick = nick_banner.replace(':cor', '35')
        elif cor_name.lower() == 'lursy':
            snick = f'echo """{name}"""|lolcat' if int_styles != '1' else f'figlet {nick}|lolcat'
        elif cor_name == '8':
            break
        else:
            print(f'{ve}{snick} não é um comando')
            sleep(2)
            os.system('clear')
            break
        nick_file = open('.Nick', 'w')
        nick_file.write(f'{snick}')
        nick_file.close()
        rnick = open('.Nick', 'r')
        bash = open('bash.bashrc', 'w')
        bash.write(f'{inicio}\n' + f'{rsenha.read()}\n{rnick.read()}\n{rcor.read()}'if vs
                   else f'{rnick.read()}\n{rcor.read()}\n{final}')
        bash.close()
        break
