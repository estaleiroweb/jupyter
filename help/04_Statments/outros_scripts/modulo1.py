
from .modulo2 import func2  # caminho relativo a esse script
from scr import func  # raiz do módulo

print("Script do módulo 1")


def func1():
    print("### Função do outros_scripts.módulo 1")


func()
func2()

# fmt: off
if False:
    import os
    import sys
    import scr
    # Adiciona o diretório pai ao sys.path
    sys.path.append(os.path.abspath(".."))

    # Agora podemos importar normalmente

    # Chamando alguma função do script importado (se existir)
    # script_a_importar.alguma_funcao()
# fmt: on
