"""Criando Barras de Progresso

Ótimo para operações demoradas
"""
import time
import click


@click.command()
def processar():
    with click.progressbar(range(100), label="Processando...") as barra:
        for i in barra:
            time.sleep(0.05)  # Simula um processamento


if __name__ == "__main__":
    processar()
