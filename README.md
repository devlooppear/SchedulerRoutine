# RotinaScheduler

- O projeto tem como objetivo permitir a configuração de mensagens para serem exibidas em horários pré-determinados pelo usuário, mas não só isso, a partir dele é possível padronizar outras tarefas de rotina em uma aplicação Flask.

## Configuração
Antes de rodar a aplicação, é necessário criar um banco de dados PostgreSQL e configurar o arquivo config.py com as informações de conexão.

Isso pode ser feito no arquivo `config.py`:
```python
DATABASE = 'mensagensrotina'
PORTA = '5432'
SENHA = '<sua senha aqui>'

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "efdhaqerhaertunterterdgv"
SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{SENHA}@localhost:{PORTA}/{DATABASE}"
```
Para criar as tabelas do banco de dados, execute os seguintes passos:

- Crie uma Database no Postgres chamado `mensagensrotina`

- Execute o seguinte comando com SQL:

```sql
CREATE TABLE rotina (
    id SERIAL PRIMARY KEY NOT NULL,
    horario VARCHAR(10) NOT NULL,
    mensagem VARCHAR(100) NOT NULL,
);
```

## Execução
Para executar a aplicação, execute o seguinte execute o arquivo `run.py`

## Resultado
Para ver o resultado dê um 'refresh' na página no determinado horário. Para fazer isso, clique no botão semelhante a uma seta que forma um circulo na região superior esquerna, na barra de navegação do seu navegador.

## Uso
Configuração de Tarefas
Na página inicial da aplicação (/), na paginá inicial ìndex.html`, o usuário pode configurar novas tarefas para exibir mensagens em horários específicos. Para isso, basta preencher os campos "Horário" e "Mensagem" no formulário e clicar em "Configurar". A mensagem será exibida no horário especificado.

## Listagem de Tarefas
As tarefas configuradas são listadas no banco de dados e podem ser acessadas através da tabela rotina.

## Execução das Tarefas
As tarefas configuradas são executadas através da biblioteca schedule. As mensagens são exibidas através do método imprimir_mensagem, que é chamado no horário especificado pelo usuário. O método iniciar_scheduler é executado em uma thread para permitir a execução das tarefas em segundo plano.
