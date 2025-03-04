"""Criando Menus de Escolha (type=click.Choice())

Podemos restringir valores de uma opção.
"""
import click

@click.command()
@click.option("--cor", type=click.Choice(["vermelho", "azul", "verde"]), help="Escolha uma cor")
def escolher_cor(cor):
    click.echo(f"Você escolheu a cor {cor}!")

if __name__ == "__main__":
    escolher_cor()
