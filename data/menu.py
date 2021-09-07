from Persux.data.ferramentas import figlet
from Persux.data.cores_persux import *


# Menus
menu_cores = f'''{ve}┏━━━━━━━━━━━━━━━━━━━┓
  {am}[ 1 ] {br}-{ve} Vermelho
  {am}[ 2 ] {br}-{am} Amarelo
  {am}[ 3 ] {br}- Branco
  {am}[ 4 ] {br}-{vd} Verde
  {am}[ 5 ] {br}-{cy} Ciano
  {am}[ 6 ] {br}-{az} Azul
  {am}[ 7 ] {br}-{rx} Roxo
  {am}[ 8 ] {br}- Voltar{ve}
┗━━━━━━━━━━━━━━━━━━━┛'''

styles = f'''{ve}┏━━━━━━━━━━━━━━━━━━━┓
  {am}[ 1 ] {br}-{cy} comum
  {am}[ 2 ] {br}-{cy} poison 
  {am}[ 3 ] {br}-{cy} lean
  {am}[ 4 ] {br}-{cy} block
  {am}[ 5 ] {br}-{cy} alligator
  {am}[ 6 ] {br}-{cy} cosmic
  {am}[ 7 ] {br}-{cy} rozzo{ve}
┗━━━━━━━━━━━━━━━━━━━┛'''

ban_sen = f'''{ve}┏━━━━━━━━━━━━━━━━━┓
  {am}[ 1 ] {br}-{cy} alterar
  {am}[ 2 ] {br}-{cy} remover
  {am}[ 3 ] {br}-{cy} voltar
{ve}┗━━━━━━━━━━━━━━━━━┛'''


menu_nome = f'''{ve}┏━━━━━━━━━━━━━━━━━━━━━━┓
  {am}[ 1 ] {br}-{cy} alterar nome
  {am}[ 2 ] {br}-{cy} voltar
{ve}┗━━━━━━━━━━━━━━━━━━━━━━┛'''

# Figlet
persuxf = f"{rx}{figlet.renderText('Persux')}"
coresf = f"{az}{figlet.renderText('Cores')}"
bannerf = f"{ve}{figlet.renderText('Banner')}"
senhaf = f"{vd}{figlet.renderText('Senha')}"
