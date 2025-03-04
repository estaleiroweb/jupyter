"""O click suporta vários tipos de dados:

| Tipo  | Exemplo                                |
| ----- | -------------------------------------- |
| str   | @click.argument("nome", type=str)      |
| int   | @click.option("--idade", type=int)     |
| float | @click.option("--altura", type=float)  |
| bool  | @click.option("--debug", is_flag=True) |

Podemos definir valores padrão usando default=.
"""
import click

@click.command()
@click.option("--idade", type=int, default=12, help="Sua idade")
def exibir_idade(idade):
    click.echo(f"Idade: {idade}")

if __name__ == "__main__":
    exibir_idade()
