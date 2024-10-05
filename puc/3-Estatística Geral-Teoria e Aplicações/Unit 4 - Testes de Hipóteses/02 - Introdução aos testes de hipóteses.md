# Introdução aos testes de hipóteses

Um teste de hipóteses é um procedimento em que utilizamos resultados experimentais provenientes de uma amostra para verificar se, uma afirmação sobre uma população, mais especificamente sobre um parâmetro dessa população, é contrariada ou não

Vamos entender alguns conceitos básicos sobre os testes de hipóteses que serão utilizados em todos os testes ao longo dessa unidade.

## Hipóteses Estatísticas

Hipótese nula (denotada por $H_0$ ) é uma hipótese estatística que contém uma afirmativa
de igualdade e deve escrever como $=$, $\leq$ ou $\geq$.

_Para uma média_, temos as três formas possíveis para a hipótese nula:
Onde, $\mu_0$ é algum valor que você deseja testar.

- $H_0: \mu = \mu_0$
- $H_0: \mu \geq \mu_0$
- $H_0: \mu \leq \mu_0$

_Para uma proporção_, temos as três formas possíveis para a hipótese nula:
Onde, $p_0$ é algum valor que você deseja testar.

- $H_0: p = p_0$
- $H_0: p \geq p_0$
- $H_0: p \leq p_0$

**Hipótese alternativa** (denotada por $H_a$ ) é o complemento da hipótese nula. É uma
afirmativa que deve ser verdadeira se $H_0$ for falsa e contém uma afirmativa de
desigualdade, tal como $<$, $\neq$ ou $>$.

_Para uma média_, a hipótese alternativa comporta apenas uma das três formas:

- $H_a \mu \neq \mu_0$
- $H_a \mu < \mu_0$
- $H_a \mu > \mu_0$

_Para uma proporção_, a hipótese alternativa comporta apenas uma das três formas:

- $H_a: p \neq p_0$
- $H_a: p < p_0$
- $H_a: p > p_0$

### Tipos de erros

| Decisão        | $H_0$ True                     | $H_0$$H_0$ False              |
| -------------- | ------------------------------ | ----------------------------- |
| Aceitar $H_0$  | Decisão correta (1 - $\alpha$) | Erro do tipo II $\beta$       |
| Rejeitar $H_0$ | Erro do tipo I $\alpha$        | Decisão correta (1 - $\beta$) |

!!! info Nível de Significância

    O **nível de significância** ($\alpha$) de um teste é a probabilidade de uma hipótese nula ser rejeitada, quando verdadeira

    | Nível de Confiança | Nivel de Significância |
    | :----------------: | :--------------------: |
    |   (1 - $\alpha$)   |       ($\alpha$)       |
    |        95%         |           5%           |
    |        98%         |           2%           |

!!! info Estatística de Teste

    A **estatística de teste** é uma estatística amostral, ou um valor baseado nos dados amostrais. Utiliza-se uma estatística de teste para tomar uma decisão sobre a rejeição ou não da hipótese nula.

!!! info Valor p

    _O valor p quantifica o erro cometido ao rejeitar a hipótese nula_. Um valor p muito pequeno sugere que os resultados amostrais são muito improváveis sob a hipótese nula, ou seja, constitui evidência contra a hipótese nula.

    O critério de decisão baseado no valor p é feito da seguinte maneira:
    
    - Rejeitar a hipótese nula ($H_0$) se o valor p é no máximo igual ao nível de significância ($\alpha$).
    - Não rejeitar a hipótese nula ($H_0$) se o valor p é maior do que o nível de significância ($\alpha$).

### Teste de hipóteses para uma média

!!! info Denominação

    - $H_0: \mu = \mu_0 \ \ \text{ou} \ \ H_a \mu \neq \mu_0 \rightarrow \text{Hipótese bilateral ou bicaudal}$
    - $H_0: \mu \geq \mu_0 \ \ \text{ou} \ \ H_a \mu < \mu_0 \rightarrow \text{Hipótese unilateral à esquerda}$
    - $H_0: \mu \leq \mu_0 \ \ \text{ou} \ \ H_a \mu > \mu_0 \rightarrow \text{Hipótese unilateral à direita}$

!!! info Testes

    *Utilizada quando $\sigma$ é conhecido!*
    $$
    z_{\text{teste}} = \frac{\bar{x} - \mu_0}{\frac{\sigma}{\sqrt{n}}}
    $$

    *Utilizada quando $\sigma$ NÃO é conhecido!*
    $$
    t_{\text{teste}} = \frac{\bar{x} - \mu_0}{\frac{s}{\sqrt{n}}}
    $$

!!! info Valor p

    | Tipo de teste       | Valor p                                                |
    | ------------------- | ------------------------------------------------------ |
    | Unilateral direito  | Área à direita da estatística de teste                 |
    | Bilateral           | 2 x a área à direita do módulo da estatística de teste |
    | Unilateral esquerdo | Área à esquerda da estatística de teste                |

### Teste de hipóteses para uma proporção

!!! info Denominação

    - $H_0: p = p_0 \ \ \text{ou} \ \ H_a: p \neq p_0 \rightarrow \text{Hipótese bilateral ou bicaudal}$
    - $H_0: p \geq p_0 \ \ \text{ou} \ \ H_a: p < p_0 \rightarrow \text{Hipótese unilateral à esquerda}$
    - $H_0: p \leq p_0 \ \ \text{ou} \ \ H_a: p > p_0 \rightarrow \text{Hipótese unilateral à direita}$

!!! info Testes

    $$
    z_{\text{teste}} = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0 (1 - p_0)}{n}}}
    
    \rightarrow

    \begin{matrix}
    n \cdot p_0 \geq 5 \\
    e \\
    n \cdot (1 - p_0) \geq 5 \\
    \end{matrix}
    $$

!!! info Valor p

    | Tipo de teste       | Valor p                                                |
    | ------------------- | ------------------------------------------------------ |
    | Unilateral direito  | Área à direita da estatística de teste                 |
    | Bilateral           | 2 x a área à direita do módulo da estatística de teste |
    | Unilateral esquerdo | Área à esquerda da estatística de teste                |
