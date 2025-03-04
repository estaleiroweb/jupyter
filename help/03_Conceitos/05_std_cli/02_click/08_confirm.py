"""Confirmação do Usuário

Podemos solicitar confirmação antes de continuar
"""
import click

@click.command()
@click.confirmation_option(prompt="Deseja realmente continuar?", default='Y')
def deletar():
    click.echo("Item deletado!")

if __name__ == "__main__":
    deletar()
