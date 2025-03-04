import argparse

"""
## Tipos de Dados

| Tipo    | Exemplo                                               |
| ------- | ----------------------------------------------------- |
| `int`   | `parser.add_argument("idade", type=int)`              |
| `float` | `parser.add_argument("altura", type=float)`           |
| `bool`  | `parser.add_argument("--debug", action="store_true")` |
"""
parser = argparse.ArgumentParser(description="Muitos exemplos de argparse")

# argumento obrigatório posicional
parser.add_argument(
    "nome",
    help="Nome da pessoa"
)
parser.add_argument(
    "sobrenome",
    # required=True,  # usado apenas com não posicionais
    help="Sobrenome da pessoa"
)

# argumento obrigatório não posicional
# parser.add_argument(
#     "--sb",
#     required=True,  # usado com múltiplas flags
#     help="Sobrenome da pessoa"
# )

# Adicionando Opções (`--flag`) e Tipos de Dados (`--type=`)
parser.add_argument(
    "--altura",
    type=float,
    help="Altura em metros"
)
parser.add_argument(
    "--idade",
    type=int,
    help="Idade da pessoa"
)

# Definindo Valores Padrão (default=)
parser.add_argument(
    "--pais",
    default="Brasil",
    help="País de origem"
)

# Opções Booleanas (store_true) e múltiplas flags (`--flag=`)
parser.add_argument(
    "-v", "--verbose", "--verb",
    action="store_true",
    help="Ativa modo detalhado"
)

# Destino/var stored
parser.add_argument(
    "-q",
    action="store_true",
    dest="quite",
    help="Ativa modo detalhado"
)
# Escolhendo Valores Fixos (`choices=`)
parser.add_argument(
    "--cor", choices=["vermelho", "azul", "verde"],
    help="Escolha uma cor"
)

# Criando Múltiplos Comandos (`subparsers`)
#
# Tente:
#
# - `script.py  --help`
# - `script.py adicionar --help`
# - `script.py remover --help`
# - `script.py primeiro_nome sobre_nome adicionar "Estudar Python"`
# - `script.py primeiro_nome sobre_nome remover "Estudar Python"`
subparsers = parser.add_subparsers(dest="comando")

# Comando 'adicionar'
adicionar_parser = subparsers.add_parser(
    "adicionar",
    help="Adiciona uma tarefa"
)
adicionar_parser.add_argument(
    "tarefa",
    help="Nome da tarefa a ser adicionada"
)

# Comando 'remover'
remover_parser = subparsers.add_parser(
    "remover",
    help="Remove uma tarefa"
)
remover_parser.add_argument(
    "tarefa",
    help="Nome da tarefa a ser removida"
)

# Veja no summary
#
# - Mensagens de Erro Personalizadas

args = parser.parse_args()
print(args)
