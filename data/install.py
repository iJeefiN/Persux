import os


def install():
    global nms
    os.chdir('/data/data/com.termux/files/usr/etc/')
    Ver = os.path.exists('.usuario')
    if not Ver:
        os.system('clear')
        user = str(input(f'\033[0;32mNome: \033[0;31m'))
        os.system('clear')
        print(f'\033[0;32minstalando.', end='')
        os.system('pkg install figlet -y &>/dev/null')
        print('.', end='')
        os.system('pip install lolcat &>/dev/null')
        print('.')
        os.system('clear')
        os.chdir('/data/data/com.termux/files/usr/etc/')
        os.system('rm -rf .Cor')
        cor = open('.Cor', 'w')
        cor.write(f"PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
        cor.close()
        os.system('rm -rf motd')
        os.chdir('/data/data/com.termux/files/usr/etc')
        user_file = open('.usuario', 'w')
        user_file.write(user)
        user_file.close()
        os.system('clear')
        nms = 1
