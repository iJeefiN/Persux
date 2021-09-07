from data.ferramentas import *
from data.menu import *


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
                clear()
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
                clear()
                break
            else:
                print(f'{ve}{ban_exists} não é um comando')
                sleep(2)
                break
        os.system('clear')
        print(bannerf)
        nick = str(input(f'{am}Nick: {br}'))
        clear()
        print(f"{rx}{figlet.renderText('Styles')}")
        print(styles)
        print(f'{vd}[i] {br}formatação do banner\n')
        int_styles = str(input(f'\n{am}//: {br}'))
        if int_styles == '1':
            name = figlet.renderText(f'{nick}')
        elif int_styles == '2':
            name = poison.renderText(f'{nick}')
        elif int_styles == '3':
            name = lean.renderText(f'{nick}')
        elif int_styles == '4':
            name = block.renderText(f'{nick}')
        elif int_styles == '5':
            name = alligator.renderText(f'{nick}')
        elif int_styles == '6':
            name = cosmic.renderText(f'{nick}')
        elif int_styles == '7':
            name = rozzo.renderText(f'{nick}')
        else:
            print(f'{ve}Comando não identificado!')
            sleep(2)
            break
        clear()
        sleep(1)
        print(f'{vd}\nbanner selecionado\n\n{br}{name}')
        sleep(2)
        banner = open('banner', 'w')
        banner.write(f'{name}'.rstrip())
        banner.close()
        clear()
        cat_banner = '''echo -e '\e[0;:corm'
cat /data/data/com.termux/files/usr/etc/banner
echo -e '\e[m\\n\\n' '''
        clear()
        print(f"{az}{figlet.renderText('Cores')}")
        print(menu_cores)
        print(f'{vd}[i] {br}cor do banner\n')
        cor_name = str(input(f'\n{am}//: {br}'))
        if cor_name == '1':
            snick = cat_banner.replace(':cor', '31')
        elif cor_name == '2':
            snick = cat_banner.replace(':cor', '33')
        elif cor_name == '3':
            snick = cat_banner.replace(':cor', '37')
        elif cor_name == '4':
            snick = cat_banner.replace(':cor', '32')
        elif cor_name == '5':
            snick = cat_banner.replace(':cor', '36')
        elif cor_name == '6':
            snick = cat_banner.replace(':cor', '34')
        elif cor_name == '7':
            snick = cat_banner.replace(':cor', '35')
        elif cor_name.lower() == 'lursy':
            snick = f"cat /data/data/com.termux/files/usr/etc/banner|lolcat && echo -e '\\n\\n'"
        elif cor_name == '8':
            break
        else:
            print(f'{ve}{cor_name} não é um comando')
            sleep(2)
            clear()
            break
        os.system('rm -rf bash.bashrc')
        nick_file = open('.Nick', 'w')
        nick_file.write(f'{snick}')
        nick_file.close()
        rnick = open('.Nick', 'r')
        bash = open('bash.bashrc', 'w')
        bash.write(f'{inicio}\n{rsenha.read()}\n{rnick.read()}\n{rcor.read()}\n{final}'if vs
                   else f'{inicio}\n{rnick.read()}\n{rcor.read()}\n{final}')
        bash.close()
        print(f'{vd}!Sucess!')
        sleep(1)
        break
