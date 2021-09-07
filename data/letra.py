from data.ferramentas import *
from data.cores_persux import *
from data.menu import coresf, menu_cores


def letra():
    os.system('clear')
    user = rnick = rsenha = open('.usuario', 'r')
    cor_letra = f"PS1='\[\e[0;31m\]┏(\[\e[0;34m\]{user.readline()}\[\e[0;31m\])" \
                f" [\[\e[0;32m\]\w\[\e[0;31m\]] \\n\[\e[0;31m\]┗► \[\e[1;:corm\]'"
    while True:
        clear()
        vn = os.path.exists('.Nick')
        vs = os.path.exists('.Senha')
        if vs:
            rsenha = open('.Senha', 'r')
        if vn:
            rnick = open('.Nick', 'r')
        print(coresf)
        print(menu_cores)
        print(f'{vd}[i] {br}cor da letra do terminal\n')
        cores = str(input(f'\n{am}//: {br}'))
        os.system('rm -rf bash.bashrc')
        if cores == '1':
            scor = cor_letra.replace(':cor', '31')
        elif cores == '2':
            scor = cor_letra.replace(':cor', '33')
        elif cores == '3':
            scor = cor_letra.replace(':cor', '37')
        elif cores == '4':
            scor = cor_letra.replace(':cor', '32')
        elif cores == '5':
            scor = cor_letra.replace(':cor', '36')
        elif cores == '6':
            scor = cor_letra.replace(':cor', '34')
        elif cores == '7':
            scor = cor_letra.replace(':cor', '35')
        elif cores == '8':
            break
        else:
            print(f'{ve}{cores} não é um comando')
            sleep(2)
            clear()
            break
        os.system('rm -rf .Cor')
        cor_file = open('.Cor', 'w')
        cor_file.write(f'{scor}')
        cor_file.close()
        rcor = open('.Cor', 'r')
        bash = open('bash.bashrc', 'w')
        bash.write((f'{inicio}\n{rsenha.read()}\n{rnick.read()}\n{rcor.read()}\n{final}' if vs and vn
                    else f'{inicio}\n{rsenha.read()}\n{rcor.read()}\n{final}' if not vn
                    else f'{inicio}\n{rnick.read()}\n{rcor.read()}\n{final}'))
        bash.close()
        break
