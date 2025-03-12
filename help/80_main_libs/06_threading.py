import threading

def minha_funcao():
    print("Executando após 2 segundos!")

timer = threading.Timer(2, minha_funcao)
timer.start()
print('Passei')