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
         
        nome_tabela ='ATLETAS' #selecionando tabela para aparecer
        busca = 'SELECT nome, idade, naipe, categoria, posição FROM %s' % nome_tabela #indicando colunas para puxar
        tabela = model.select_rows(cursor, busca)
        dicionarios = [] #convertendo em dicionarios

        for linha in tabela:
            dicionarios.append({'nome': linha[0], 'idade': linha [1], 'naipe': [2], 'categoria': [3], 
            'posição': linha [4] #ordem dos itens é independete pq foi selecionado apenas alguns itens para puxar
                })
        response = jsonify(dicionarios) #mandando retornar os dicionarios
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @app.route('/select_and_populate_table', methods=['POST'])
    def select_and_populate_table():
        with model.SQLite(os.path.join(db_path, db_name)) as cursor:

            nome_tabela = request.form['second_task_table_selector'] # puxando a tabela
            busca = 'SELECT * FROM %s' % nome_tabela #selecionando oq buscar das tabelas
            tabela = model.select_rows(cursor, busca)

            #convertendo em dicionarios
            dicionarios = []
            for linha in tabela:

                #colocando uma condição pq cada tabela tem colunas diferentes sem esta condição nao identifica os itens
                #Os id e codigos tiveram que permanecer pois, se excluidos teria que criar condições tambem para a busca
                #linhas tem que ser em ordem do model pois se nao desconfigura e nao roda na hr de selecionar no dropdown
                #pq foi definido que tudo das tabela viria no SELECT e nao so alguns itens

                if nome_tabela == 'ATLETAS': 
                    dicionarios.append({
                        'id_atleta': linha[0], 
                        'nome': linha[1],
                        'Idade': linha[2],
                        'id_time': linha[3],
                        'categoria': linha[4],
                        'posição': linha[5],
                        'codigo_cadastro': linha[6],
                        'país': linha[7],
                        'Naipe': linha[8],
                        'tipo': linha[9]
                    })

                elif nome_tabela == 'TECNICOS':
                    dicionarios.append({
                       'id_tecnico': linha[0],
                        'nome': linha[1],
                        'país': linha[2],
                        'id_time':linha[3],
                        'codigo_cadastro':linha[4],
                        'ja_foi_atleta': linha[5],
                        'treina_o_naipe': linha[6]
                })

                elif nome_tabela == 'TIMES':
                    dicionarios.append({
                        'id_time': linha[0],
                        'nome': linha[1],
                        'id_tecnico': linha[2],
                        'Naipe': linha[3],
                        'país': linha[4],
                        'tipo': linha[5],
                        'Competição_atual':linha[6]
                    })

                elif nome_tabela == 'ATLETA_para_TIME':
                    dicionarios.append({
                        'id_atleta': linha[0],
                        'id_time':linha[1]
                    })

                elif nome_tabela == 'TECNICO_para_TIME':
                   dicionarios.append({
                        'id_tecnico': linha[0],
                        'id_time':linha[1]
                   }) 

            response = jsonify(dicionarios) #mandando retornar os dicionarios
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

    # coloca o backend a rodar
    app.run()


if __name__ == '__main__':
    main()
