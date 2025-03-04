# Biblioteca `argparse`

O `argparse` é um **módulo padrão do Python** usado para criar **interfaces de linha de comando (CLI)**. Ele permite definir **argumentos e opções** que um usuário pode fornecer ao executar um script.  

- Aceita argumentos e opções personalizados
- Gera automaticamente mensagens de ajuda (`--help`)
- Facilita a manipulação de entrada no terminal

## 1. Criando um Script Simples com `argparse`

O exemplo abaixo aceita **um argumento obrigatório** chamado `nome` e imprime uma saudação.

```python
import argparse

# Criando o analisador de argumentos
parser = argparse.ArgumentParser(description="Script de saudação")
parser.add_argument("nome", help="Nome da pessoa")

# Lendo os argumentos passados
args = parser.parse_args()

print(f"Olá, {args.nome}!")
```

**Execução no terminal:**  

```sh
python script.py João
```

**Saída:**  

```text
Olá, João!
```

**Ajuda automática (`--help`):**  

```sh
python script.py --help
```

**Saída:**  

```text
usage: script.py [-h] nome
Script de saudação
positional arguments:
  nome        Nome da pessoa
optional arguments:
  -h, --help  show this help message and exit
```

---

## 2. Adicionando Opções (`--flag`)

As opções são argumentos que começam com `-` ou `--` e não são obrigatórios.

```python
import argparse

parser = argparse.ArgumentParser(description="Exemplo de opção")
parser.add_argument("--idade", type=int, help="Idade da pessoa")

args = parser.parse_args()

if args.idade:
    print(f"Você tem {args.idade} anos.")
else:
    print("Idade não informada.")
```

**Execução:**  

```sh
python script.py --idade 25
```

**Saída:**  

```text
Você tem 25 anos.
```

---

## 3. Argumentos Obrigatórios

Podemos definir argumentos **obrigatórios**.

```python
import argparse

parser = argparse.ArgumentParser(description="Exemplo de argumento obrigatório")
parser.add_argument("nome", help="Nome da pessoa")
parser.add_argument("sobrenome", help="Sobrenome da pessoa")

args = parser.parse_args()

print(f"Nome completo: {args.nome} {args.sobrenome}")
```

**Execução correta:**  

```sh
python script.py João Silva
```

**Erro ao não passar um argumento:**  

```sh
python script.py João
```

```text
error: the following arguments are required: sobrenome
```

---

## 4. Definindo Valores Padrão (`default=`)

Se um argumento não for passado, podemos definir um valor padrão.

```python
import argparse

parser = argparse.ArgumentParser(description="Exemplo de valores padrão")
parser.add_argument("--pais", default="Brasil", help="País de origem")

args = parser.parse_args()

print(f"Você é do {args.pais}.")
```

**Execução:**  

```sh
python script.py --pais Canadá
```

**Saída:**  

```text
Você é do Canadá.
```

**Execução sem argumento (`default="Brasil"`)**  

```sh
python script.py
```

```text
Você é do Brasil.
```

---

## 5. Opções Booleanas (`store_true`)

Para criar **flags booleanas** (ativar/desativar uma opção), usamos `store_true`.

```python
import argparse

parser = argparse.ArgumentParser(description="Exemplo de flag booleana")
parser.add_argument("--verbose", action="store_true", help="Ativa modo detalhado")

args = parser.parse_args()

if args.verbose:
    print("Modo detalhado ativado!")
else:
    print("Modo normal.")
```

**Execução no terminal:**  

```sh
python script.py --verbose
```

**Saída:**  

```text
Modo detalhado ativado!
```

---

## 6. Definindo Tipos de Dados

Podemos especificar **diferentes tipos de dados** para os argumentos.

| Tipo    | Exemplo                                               |
| ------- | ----------------------------------------------------- |
| `int`   | `parser.add_argument("idade", type=int)`              |
| `float` | `parser.add_argument("altura", type=float)`           |
| `bool`  | `parser.add_argument("--debug", action="store_true")` |

```python
parser.add_argument("idade", type=int, help="Idade da pessoa")
parser.add_argument("altura", type=float, help="Altura em metros")
```

---

## 7. Escolhendo Valores Fixos (`choices=`)

Podemos restringir os valores aceitos.

```python
parser.add_argument("--cor", choices=["vermelho", "azul", "verde"], help="Escolha uma cor")
```

**Execução válida:**  

```sh
python script.py --cor azul
```

**Execução inválida:**  

```sh
python script.py --cor roxo
```

```text
error: argument --cor: invalid choice: 'roxo'
```

---

## 8. Criando Múltiplos Comandos (`subparsers`)

Podemos criar **subcomandos**, como `git commit` e `git push`.

```python
import argparse

parser = argparse.ArgumentParser(description="Gerenciador de tarefas")
subparsers = parser.add_subparsers(dest="comando")

# Comando 'adicionar'
adicionar_parser = subparsers.add_parser("adicionar", help="Adiciona uma tarefa")
adicionar_parser.add_argument("tarefa", help="Nome da tarefa")

# Comando 'remover'
remover_parser = subparsers.add_parser("remover", help="Remove uma tarefa")
remover_parser.add_argument("tarefa", help="Nome da tarefa a ser removida")

args = parser.parse_args()

if args.comando == "adicionar":
    print(f"Tarefa '{args.tarefa}' adicionada!")
elif args.comando == "remover":
    print(f"Tarefa '{args.tarefa}' removida!")
else:
    parser.print_help()
```

**Execução no terminal:**  

```sh
python script.py adicionar "Estudar Python"
python script.py remover "Estudar Python"
```

---

## 9. Mensagens de Erro Personalizadas

Podemos modificar as mensagens de erro para torná-las mais amigáveis.

```python
parser = argparse.ArgumentParser(description="Exemplo de erro personalizado", exit_on_error=False)
parser.add_argument("idade", type=int, help="Idade da pessoa")

try:
    args = parser.parse_args()
except argparse.ArgumentError as e:
    print(f"Erro: {e}")
```

---

## **📌 Resumo Rápido: O Que o `argparse` Pode Fazer?**

| Função                                | Descrição                          |
| ------------------------------------- | ---------------------------------- |
| `ArgumentParser(description="Texto")` | Define um parser de argumentos     |
| `add_argument("nome")`                | Define um argumento obrigatório    |
| `add_argument("--flag")`              | Define uma opção (não obrigatória) |
| `type=int`                            | Converte entrada para inteiro      |
| `default="valor"`                     | Define um valor padrão             |
| `choices=["a", "b", "c"]`             | Restringe opções válidas           |
| `action="store_true"`                 | Define flags booleanas             |
| `add_subparsers()`                    | Cria subcomandos                   |

## **🚀 Conclusão**

O `argparse` é uma ferramenta essencial para **criação de CLIs profissionais** no Python. Ele facilita a manipulação de argumentos e gera documentação automaticamente.
