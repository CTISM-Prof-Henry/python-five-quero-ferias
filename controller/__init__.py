import os
import sqlite3
from flask import Flask, request, jsonify
import sys

filepath = os.path.dirname(__file__)
sys.path.append(os.path.join(filepath, '..'))

# importa módulo do banco de dados; permite prodar as funções desse módulo através da sintaxe
# model.<nome_da_função>
# por exemplo, model.select_rows
# para selecionar as linhas
import model


def get_table_column_names(cursor: sqlite3.Cursor, table_name: str) -> list:
    """
    Método que pega o nome das colunas de uma tabela no banco de dados.
    :param cursor: Um cursor para o banco de dados
    :param table_name: O nome da tabela
    :return: O nome das tabelas do banco, como uma lista
    """
    res = model.raw_execute(cursor, 'PRAGMA table_info(%s)' % table_name)
    column_names = [x[1] for x in res.fetchall()]
    return column_names


def main():
    app = Flask(__name__)  # inicia uma aplicação do flask (o backend)
    db_path = os.path.join(filepath, '..', 'model')
    db_name = 'test.db'
    # deleta & cria o banco de dados, toda vez que o backend for iniciado
    model.main(db_path, db_name)

    @app.route('/')
    def initial_page():
        # TODO atividade que vale 10 pontos adicionais!
        # TODO desenvolva uma página html no arquivo yours.html
        # TODO leia o arquivo yours.html utilizando as funcionalidades
        # TODO do python, e retorne o texto da página com este método
        return '''
        <h1>Olá mundo!</h1>
        <p>Você acessou a página inicial da Web API.</p>
        '''

    @app.route('/populate_table', methods=['POST'])
    def populate_table():
        response = jsonify([
            {
                'Nome': 'Babi Arenhart',
                'Idade': 35,
                'Time': 'Krim Mercator',
                'Categoria': 'Adulto',
                'Posição': 'Goleira',
                'País': 'Brasil',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {

                'Nome': 'Katarina Krpez',
                'Idade': 33,
                'Time': 'Krim Mercator',
                'Categoria': 'Adulto',
                'Posição': 'Ponta',
                'País': 'Servia',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Nina Zabjek',
                'Idade': 23,
                'Time': 'Krim Mercator',
                'Categoria': 'Adulto',
                'Posição': 'Central',
                'País': 'Eslovenia',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Lois Abbingh',
                'Idade': 29,
                'Time': 'Odense Handbold',
                'Categoria': 'Adulto',
                'Posição': 'Armadora',
                'País': 'França',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Kamilla Larsen',
                'Idade': 38,
                'Time': 'Odense Handbold',
                'Categoria': 'Adulto',
                'Posição': 'Pivo',
                'País': 'Dinamarca',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Freja Cohrt',
                'Idade': 27,
                'Time': 'Odense Handbold',
                'Categoria': 'Adulto',
                'Posição': 'Ponta',
                'País': 'Dinamarca',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Rikke Iversen',
                'Idade': 28,
                'Time': 'Odense Handbold',
                'Categoria': 'Adulto',
                'Posição': 'Pivo',
                'País': 'Dinamarca',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Silvia Navarro',
                'Idade': 42,
                'Time': 'Rocasa Gran Canaria ACE',
                'Categoria': 'Adulto',
                'Posição': 'Goleira',
                'País': 'Espanha',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Mizuki Hosoe',
                'Idade': 28,
                'Time': 'Rocasa Gran Canaria ACE',
                'Categoria': 'Adulto',
                'Posição': 'Central',
                'País': 'Japao',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Agni Zygoura',
                'Idade': 25,
                'Time': 'Rocasa Gran Canaria ACE',
                'Categoria': 'Adulto',
                'Posição': 'Central',
                'País': 'Grecia',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Rosana Martinez',
                'Idade': 17,
                'Time': 'Rocasa Gran Canaria ACE',
                'Categoria': 'Adulto',
                'Posição': 'Armadora',
                'País': 'Espanha',
                'Naipe': 'Feminino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Vicent Gerald',
                'Idade': 34,
                'Time': 'PSG Handball',
                'Categoria': 'Adulto',
                'Posição': 'Goleiro',
                'País': 'França',
                'Naipe': 'Masculino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Leo Villain',
                'Idade': 18,
                'Time': 'PSG Handball',
                'Categoria': 'Adulto',
                'Posição': 'Goleiro',
                'País': 'França',
                'Naipe': 'Masculino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Loik Spady',
                'Idade': 21,
                'Time': 'PSG Handball',
                'Categoria': 'Adulto',
                'Posição': 'Goleiro',
                'País': 'França',
                'Naipe': 'Masculino',
                'Tipo': 'Profissional'
            },
            {
                'Nome': 'Yann Genty',
                'Idade': 39,
                'Time': 'PSG Handball',
                'Categoria': 'Adulto',
                'Posição': 'Goleiro',
                'País': 'França',
                'Naipe': 'Masculino',
                'Tipo': 'Profissional'
            }
        ])

        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @app.route('/select_and_populate_table', methods=['POST'])
    def select_and_populate_table():
        with model.SQLite(os.path.join(db_path, db_name)) as cursor:
            tabela = request.form['second_task_table_selector']
            response = jsonify([
                tabela.execute("SELECT * FROM ATLETAS")
                for row in tabela: 
                print("* {Name}".format(Name=row['ATLETAS']
                ]) 
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

    # coloca o backend a rodar
    app.run()


if __name__ == '__main__':
    main()
