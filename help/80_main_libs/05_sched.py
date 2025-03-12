"""O módulo sched permite agendar uma função para ser executada no futuro"""

import sched
import time

def minha_funcao():
    print("Executando a função após 2 segundos!")

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(2, 1, minha_funcao)  # Agenda a função para rodar em 2 segundos
scheduler.run()
print('Passei')
