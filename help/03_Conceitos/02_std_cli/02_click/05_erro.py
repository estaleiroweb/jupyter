"""Personalizando Mensagens de Erro

Podemos definir mensagens personalizadas em caso de erro.
"""
import click

@click.command()
@click.option("--idade", type=int, default=12)
def verificar(idade):
    if idade < 18:
        raise click.BadParameter("Você deve ter pelo menos 18 anos.")
    click.echo(f"Idade aceita: {idade}")


if __name__ == "__main__":
    verificar()
