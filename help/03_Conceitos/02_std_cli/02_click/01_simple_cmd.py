"""Criando um Comando Simples

O click torna a criação de comandos simples e intuitiva.
"""
import click


@click.command()
@click.option("--nome", prompt="Digite seu nome", help="Seu nome")
def saudacao(nome):
    click.echo(f"Olá, {nome}!")


if __name__ == "__main__":
    saudacao()
