"""Senhas e Entradas Ocultas

Usamos click.prompt() para solicitar valores sensíveis
"""
import click

@click.command()
def senha():
    senha = click.prompt("Digite sua senha", hide_input=True)
    click.echo("Senha salva com sucesso!")

if __name__ == "__main__":
    senha()
