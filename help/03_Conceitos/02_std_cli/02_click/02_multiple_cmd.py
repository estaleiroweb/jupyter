"""Criando Múltiplos Comandos (Grupo de Comandos)

Com o click, podemos definir múltiplos comandos dentro de um mesmo script.
"""
import click


@click.group()
def cli():
    """Grupo de comandos CLI"""
    pass


@cli.command()
def ola():
    """Diz Olá!"""
    click.echo("Olá, Mundo!")


@cli.command()
@click.argument("nome")
def saudacao(nome):
    """Saúda a pessoa pelo nome"""
    click.echo(f"Olá, {nome}!")

@cli.command()
@click.option("--verbose", is_flag=True, help="Modo detalhado")
def exibir(verbose):
    "Modo verbose"
    if verbose:
        click.echo("Modo detalhado ativado!")
    else:
        click.echo("Modo normal.")

if __name__ == "__main__":
    cli()
