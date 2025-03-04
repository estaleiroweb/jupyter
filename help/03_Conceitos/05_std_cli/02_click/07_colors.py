"""Formatando Saídas com Cores

O click permite exibir mensagens coloridas no terminal
"""
import click

@click.command()
def mensagem():
    click.secho("Erro!", fg="red", bold=True)
    click.secho("Aviso!", fg="yellow")
    click.secho("Sucesso!", fg="green")

if __name__ == "__main__":
    mensagem()
