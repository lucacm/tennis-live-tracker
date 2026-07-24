Semana 3 — APIs, Git e projeto âncora

O que estudar

Usar UV ou Poetry
HTTP básico: GET, POST, headers, status codes
requests: .get(), .post(), .json()
Variáveis de ambiente com python-dotenv
Git: init, add, commit, push
GitHub: criar repositório, fazer push


Como praticar


Chamar a API pública do GitHub (sem auth) e imprimir repos
Chamar API com API key via .env
Commitar cada exercício da semana no GitHub
Ler um erro 401 e entender o que significa


Mini-exercícios


Buscar dados de uma API pública (clima, moeda etc.)
Salvar resposta JSON em arquivo local
Publicar o script no GitHub com README de 5 linhas


Ponte mental


No RPA, você usava um conector HTTP pronto. Em Python, você constrói esse conector em 5 linhas com requests — e pode inspecionar cada detalhe da requisição e resposta.



Entrega da semana

Projeto âncora publicado no GitHub.


Projeto âncora — detalhamento

Descrição: Script que chama uma API de cotação de moedas, compara com um threshold e salva alerta em JSON.

PassoO que fazer1. Configurar ambienteCriar pasta, venv, instalar requests e python-dotenv, criar .env com API key2. Chamar a APIUsar requests.get() para buscar cotação atual do USD/BRL, imprimir resposta crua3. Processar resultadoExtrair valor do JSON com .json()["rate"], comparar com threshold em variável4. Salvar e publicarEscrever resultado (data, valor, status alerta) em resultado.json, commitar no GitHub

APIs públicas gratuitas sugeridas:


Câmbio: https://api.exchangerate.host/latest?base=USD
Teste de JSON: https://api.github.com/users/{username}


Checkpoint de validação

O tech lead consegue clonar o repo, rodar python main.py e ver o resultado.json gerado — sem explicação verbal.