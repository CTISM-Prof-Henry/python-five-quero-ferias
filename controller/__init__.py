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
     with model.SQLite(os.path.join(db_path, db_name)) as cursor:
        nome_tabela ='ATLETAS'
        busca = 'SELECT nome, idade, naipe, categoria, posição FROM %s' % nome_tabela
        tabela = model.select_rows(cursor, busca)
        dicionarios = []
        for linha in tabela:
            dicionarios.append({'nome': linha[0], 'idade': linha [1], 'naipe': [2], 'categoria': [3], 'posição': linha [4]
                })
        response = jsonify(dicionarios)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @app.route('/select_and_populate_table', methods=['POST'])
    def select_and_populate_table():
        with model.SQLite(os.path.join(db_path, db_name)) as cursor:
            nome_tabela = request.form['second_task_table_selector'] # puxei a tabela
            busca = 'SELECT nome, naipe, idade, id_time, categoria, posição FROM %s' % nome_tabela #selecionei oq qr buscar das tabelas
            tabela = model.select_rows(cursor, busca) 
        #convertendo em dicionarios:
            dicionarios = []
            for linha in tabela:
                dicionarios.append({'nome': linha[0], 'naipe': linha [1], 'Idade': linha [2],
                'id_time': linha [3], 'categoria': linha [4], 'posição': linha [5],
                })
            response = jsonify(dicionarios)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

    # coloca o backend a rodar
    app.run()


if __name__ == '__main__':
    main()
