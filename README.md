# pythonFive

## Atenção

**Leia com atenção as instruções deste README.**

Este trabalho não é difícil por si só, porém dada a complexidade, é muito fácil cometer erros que podem desconfigurar
todo o projeto.

Portanto, faça commits constantemente. Tão logo implemente uma versão funcional do seu código, salve-o com os comandos
do git:

```bash
git add .
git commit -m "implementei uma função no meu código"
git push origin main
```

Se você fizer alguma coisa que desconfigure o projeto, você pode sempre descartar **todas** as modificações feitas no
código:

```bash
git reset
```

Ou então, se o problema for **realmente sério**, você pode voltar para um commit anterior com o comando:

```bash
git reset --hard <hash do commit>
```

Você pode pegar a hash do commit no site do seu repositório, no Github.

## Como rodar o controller

### Instruções para a linha de comando

1. Clone este repositório na sua máquina:
   ```bash
   git clone https://github.com/<seu nome de usuário>/<nome do repositório>.git
   ```
2. Entre na pasta do repositório, na sua máquina local:
   ```bash
   cd <nome do repositório>
   ```
3. A partir desta pasta, rode o seguinte comando na linha de comando:
   ```bash
   python controller/__init__.py
   ```
4. Agora você já pode abrir o arquivo [view/pages/main.html](view/pages/main.html) no seu navegador.

### Instruções para o Pycharm

1. Clone este repositório na sua máquina:
   ```bash
   git clone https://github.com/<seu nome de usuário>/<nome do repositório>.git
   ```
2. Abra o Pycharm
3. Abra o projeto, pelo Pycharm: `File > Open > localize a pasta do repositório no seu computador`
4. Abra o arquivo [controller/__init__.py](controller/__init__.py)
5. Execute este arquivo pelo Pycharm
6. Agora você já pode abrir o arquivo [view/pages/main.html](view/pages/main.html) no seu navegador.

## Objetivo primário

Seu objetivo primário é desenvolver uma página Web completa, que use HTML, CSS, Javascript, AJAX, e um backend implementado
em Python. A página Web (view) deve mandar requisições para o controller. O controller faz uma consulta ao banco de dados
(model). De posse da resposta, o controller envia a resposta de volta à página Web (view). A página Web, usando AJAX, 
atualiza o seu conteúdo, mostrando ao usuário. 

Esse fluxo de trabalho é comum a várias páginas da Web. Por exemplo, quando fazemos compras online, o site da loja (view)
está fazendo esse bate-e-volta com o servidor (controller). 

### O que já está implementado?

* View:
  * O HTML principal, [main.html](view/pages/main.html) 
  * O CSS principal, [main.css](view/styles/main.css)
  * O arquivo com código Javascript e AJAX, [main.js](view/scripts/main.js) 

* Model:
  * Existe um arquivo em Python que faz acesso à um banco de dados de exemplo (arquivo 
    [model/\_\_init\_\_.py](model/__init__.py)). 
    Este arquivo é o mesmo disponível no trabalho anterior da disciplina. Você pode concluir este trabalho utilizando
    este banco de dados de teste, mas é melhor que você use o seu próprio banco de dados. Simplesmente copie e cole o código
    do trabalho anterior neste arquivo.

* Controller:
  * Um _template_ é disponibilizado no arquivo [controller/\_\_init\_\_.py](controller/__init__.py). **É neste arquivo
    que você deve mexer para concluir este trabalho.**

### Nota do objetivo principal

|                                                                                     Critério | Nota |
|:---------------------------------------------------------------------------------------------|-----:|
|                                                              Usar seu próprio banco de dados |    2 |
|                                                          Implementar a função populate_table |    2 |
|                                               Implementar a função select_and_populate_table |    2 |
|                                      As tabelas (na página HTML) **não possuem** a coluna ID |    2 |
| As opções do seletor de tabelas (na página HTML) correspondem aos nomes das tabelas do banco |    2 |

## Objetivo secundário

Seu objetivo secundário é desenvolver uma página HTML no arquivo [yours.html](view/pages/yours.html). 

Essa página deve ser a página principal do seu site; ela deve descrever o contexto do banco de dados que você 
desenvolveu no trabalho anterior (por exemplo, se o banco de dados era sobre times de futebol, esta página deve dar uma
introdução do assunto).

Essa página não conta pontos para o objetivo principal; ela possui uma pontuação própria, descrita abaixo. Você não 
precisa fazer o objetivo secundário, **porém ele vale 10 pontos adicionais na nota deste trabalho.**

### Nota do objetivo secundário

|                                                                                                 Critério | Nota |
|:---------------------------------------------------------------------------------------------------------|-----:|
|                                  A página HTML é lida de um arquivo e retornada pela função initial_page |    2 |
|                         A página HTML possui um ícone próprio (a imagem que aparece na aba do navegador) |    1 |
|                      A página HTML possui um estilo próprio (arquivo [yours.css](view/styles/yours.css)) |    2 |
|                                                                          A página HTML possui uma imagem |    1 | 
|                                                                A página HTML possui uma tabela (em HTML) |    1 |
|                                        A página HTML possui as informações centralizadas horizontalmente |    1 |
| O design da página HTML é responsivo - os itens se reajustam na página de acordo com o tamanho da janela |    2 |



## Hardware de desenvolvimento

Este trabalho foi desenvolvido no seguinte hardware. Caso você tenha problemas em rodar o código, mesmo sem ter feito
nenhuma modificação, tente adequar seu ambiente de desenvolvimento às especificações a seguir:

|                Item |                        Valor |
|:--------------------|:-----------------------------|
|    Versão do Python |                 Anaconda 3.7 |
|                 IDE | Pycharm Professional Edition | 
|       Navegador Web |                Google Chrome |
| Sistema operacional |           Windows 10 64 bits |