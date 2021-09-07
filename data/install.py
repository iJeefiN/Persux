import os
from data.cores_persux import *


def install():
    print(f'{vd}verificando atualizações')
    os.system('git pull &>/dev/null')
    os.chdir('/data/data/com.termux/files/usr/etc/')
    inst = os.path.exists('.usuario')
    if not inst:
        os.system('clear')
        user = str(input(f'{vd}Nome: {ve}'))
        os.system('clear')
        print(f'{vd}instalando.')
        os.system('python3 -m pip install --upgrade pip &>/dev/null')
        os.system('pkg install figlet -y &>/dev/null')
        os.system('clear')
        print(f'{vd}instalando..')
        os.system('pip install lolcat &>/dev/null')
        os.system('clear')
        print(f'{vd}instalando...')
        os.system('pip install pyfiglet &>/dev/null')
        os.system('clear')
        os.system('rm -rf .Cor')
        cor = open('.Cor', 'w')
        cor.write(f"PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
        cor.close()
        os.system('rm -rf motd')
        user_file = open('.usuario', 'w')
        user_file.write(user)
        user_file.close()
        os.system('clear')
