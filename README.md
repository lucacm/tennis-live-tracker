# API Week 3 — Tennis Live Score

Script que consulta a API de tênis ao vivo (RapidAPI) para verificar se um
jogador está jogando no momento e salva o resultado em [resultado.json](resultado.json).
Por padrão verifica o "Alcaraz", mas aceita o nome de qualquer jogador como argumento.

## Pré-requisitos

- Python >= 3.14
- [uv](https://docs.astral.sh/uv/) instalado
- Uma chave de API da [Tennis Live Data (RapidAPI)](https://rapidapi.com/)

## Como rodar

1. Clone o repositório e entre na pasta do projeto:

   ```bash
   git clone <url-do-repositorio>
   cd api_week3
   ```

2. Copie o arquivo de exemplo de variáveis de ambiente e preencha com sua chave:

   ```bash
   cp .env.example .env
   ```

   Depois edite o `.env` e defina o valor de `RAPIDAPI_KEY`.

3. Instale as dependências (o `uv` cria o virtualenv automaticamente):

   ```bash
   uv sync
   ```

4. Execute o script:

   ```bash
   uv run tennis.py
   ```

   Para verificar outro jogador, passe o nome (ou parte dele) como argumento:

   ```bash
   uv run tennis.py burruchaga
   ```

5. Confira o resultado gerado em [resultado.json](resultado.json).

## Argumentos

| Argumento | Obrigatório | Padrão    | Descrição                                  |
| --------- | ------------ | --------- | ------------------------------------------- |
| `jogador` | Não          | `Alcaraz` | Nome (ou parte do nome) do jogador a buscar entre as partidas ao vivo |

## Variáveis de ambiente

| Variável       | Descrição                                  |
| -------------- | ------------------------------------------- |
| `RAPIDAPI_KEY` | Chave de API do RapidAPI para o endpoint de tênis ao vivo |

## Estrutura do projeto

```
main.py          # API FastAPI de exemplo (não faz parte do fluxo do tennis.py)
tennis.py         # Script principal: consulta a API e gera resultado.json
resultado.json     # Saída gerada pela última execução do tennis.py
.env.example       # Modelo de variáveis de ambiente
```
