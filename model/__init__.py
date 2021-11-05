import os
import sqlite3


class SQLite( object ):
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect( self.file )
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


def create_table(cursor: sqlite3.Cursor, table: str, fields: dict, other_data: list = None) -> None:

    command = "CREATE TABLE %s (%s)" % (
        table,
        ','.join( [k + ' ' + v for k, v in fields.items()] + (
            other_data if other_data is not None else []) )
    )
    cursor.execute( command )


def insert_rows(cursor: sqlite3.Cursor, table: str, tuples: list) -> None:

    for some_tuple in tuples:
        tuple_values = []
        for v in some_tuple.values():
            if isinstance( v, str ):
                tuple_values += ['\'' + v + '\'']
            else:
                tuple_values += [str( v )]

        command = "INSERT INTO %s(%s) VALUES (%s)" % (
            table, ','.join( map( str, some_tuple.keys() ) ), ','.join( tuple_values )
        )
        cursor.execute( command )


def select_rows(cursor: sqlite3.Cursor, clause: str) -> list:

    res = cursor.execute( clause )
    rows = []
    for row in res:  # type: sqlite3.Row
        rows += [tuple( [row[k] for k in row.keys()] )]

    return rows


def raw_execute(cursor: sqlite3.Cursor, clause: str) -> sqlite3.Cursor:

    return cursor.execute( clause )


def remove_db(file: str) -> None:

    try:
        os.remove( file )
    except FileNotFoundError:
        pass


def main(path: str = '.', db_name: str = 'test.db') -> None:
    remove_db( os.path.join( path, db_name ) )

    with SQLite( os.path.join( path, db_name ) ) as cursor:
        # todas as tabelas possuem mais de 4 colunas
        # foram feitas mais de 4 tabelas


        create_table(
            cursor,
            'ATLETAS',  # tabela com 10 tuplas (no caso acho que tem mais)
            {
                'id_atleta': 'INTEGER PRIMARY KEY', 'nome': 'text NOT NULL', 'Idade': 'INTEGER NULL',
                'id_time': 'INTEGER NULL', 'categoria': 'text NOT NULL', 'posição': 'text NOT NULL',
                'codigo_cadastro': 'INTEGER NULL', 'país': 'text NOT NULL', 'Naipe': 'text NOT NULL',
                'tipo': 'text NOT NULL'}
        )

        create_table(
            cursor,
            'TIMES',
            {
                'id_time': 'INTEGER PRIMARY KEY', 'nome': 'text NOT NULL', 'id_tecnico': 'INTEGER NULL',
                'Naipe': 'text NOT NULL', 'país': 'text NOT NULL',
                'tipo': 'text NOT NULL', 'Competição_atual': 'text NULL'}
        )

        create_table(
            cursor,
            'TECNICOS',
            {
                'id_tecnico': 'INTEGER PRIMARY KEY', 'nome': 'text NOT NULL', 'país': 'text NOT NULL',
                'id_time': 'INTEGER NULL', 'codigo_cadastro': 'INTEGER NULL', 'ja_foi_atleta': 'text NOT NULL',
                'treina_o_naipe': 'text NOT NULL'
            }
        )

        create_table(  # tabela com chave composta e estrangeira
            cursor,  # tabela de conexao entre a atletas e times interligando o id de cada um inserido
            'ATLETA_para_TIME',
            {'id_atleta': 'INTEGER NOT NULL', 'id_time': 'INTEGER NOT NULL'},
            ['PRIMARY KEY(id_atleta, id_time)', 'FOREIGN KEY(id_atleta) REFERENCES atleta(id)',
             'FOREIGN KEY(id_time) REFERENCES time(id)']
        )

        create_table(  # tabela com chave composta e estrangeira
            cursor,  # tabela de conexao entre tecnico e time interligando o id de cada um inserido
            'TECNICO_para_TIME',
            {'id_tecnico': 'INTEGER NOT NULL', 'id_time': 'INTEGER NOT NULL'},
            ['PRIMARY KEY(id_tecnico, id_time)', 'FOREIGN KEY(id_tecnico) '
            'REFERENCES tecnico(id)', 'FOREIGN KEY(id_time) REFERENCES time(id)'] )

        insert_rows(   #inserindo os dados da tebela tecnico
            cursor,
            'TECNICOS',
            [
                {
                    #krim mercator
                    'id_tecnico': 20211,
                    'nome': 'Natalia Derepasko',
                    'país': 'Eslovenia',
                    'id_time': 2021201,
                    'codigo_cadastro': 202112021201,
                    'ja_foi_atleta': 'Sim',
                    'treina_o_naipe': 'Feminino'
                },
                {
                    #Odense Handebold
                    'id_tecnico': 20212,
                    'nome': 'Ulrik Kirkely',
                    'país': 'Dinamarca',
                    'id_time': 2021202,
                    'codigo_cadastro': 202122021202,
                    'ja_foi_atleta': 'Sim',
                    'treina_o_naipe': 'Feminino'
                },
                {
                    #Rocasa Gran Canaria
                    'id_tecnico': 20213,
                    'nome': 'Robert Cuesta',
                    'país': 'Espanha',
                    'id_time': 2021203,
                    'codigo_cadastro': 202132021203,
                    'ja_foi_atleta': 'Sim',
                    'treina_o_naipe': 'Feminino'
                },
                {
                    #PSG
                    'id_tecnico': 202104,
                    'nome': 'Regis Boxele',
                    'país': 'França',
                    'id_time': 2021301,
                    'codigo_cadastro': 2021042021301,
                    'ja_foi_atleta': 'Sim',
                    'treina_o_naipe': 'Masculino'
                },
                {
                    #RK
                    'id_tecnico': 202105,
                    'nome': 'Miodrag Kazic',
                    'país': 'Montenegro',
                    'id_time': 2021302,
                    'codigo_cadastro': 2021052021302,
                    'ja_foi_atleta': 'Sim',
                    'treina_o_naipe': 'Masculino'
                },
                {
                    #Bevo HC
                    'id_tecnico': 202106,
                    'nome': 'Peter Kersten',
                    'país': 'Paises Baixos',
                    'id_time': 2021303,
                    'codigo_cadastro': 2021062021303,
                    'ja_foi_atleta': 'Sim',
                    'treina_o_naipe': 'Masculino'
                },
            ]
        )

        insert_rows( #inserindo os dados da tabela atleta
            cursor,
            'ATLETAS',
            [
                {
                    'id_atleta': 2021001,
                    'nome': 'Babi Arenhart',
                    'Idade': 35,
                    'id_time': 2021201,
                    'categoria': 'Adulto',
                    'posição': 'Goleira',
                    'codigo_cadastro': 20210012021201,
                    'país': 'Brasil',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021002,
                    'nome': 'Katarina Krpez',
                    'Idade': 33,
                    'id_time': 2021201,
                    'categoria': 'Adulto',
                    'posição': 'Ponta',
                    'codigo_cadastro': 20210022021201,
                    'país': 'Servia',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021003,
                    'nome': 'Nina Zabjek',
                    'Idade': 23,
                    'id_time': 2021201,
                    'categoria': 'Adulto',
                    'posição': 'Central',
                    'codigo_cadastro': 20210032021201,
                    'país': 'Eslovenia',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021104,
                    'nome': 'Lois Abbingh',
                    'Idade': 29,
                    'id_time': 2021202,
                    'categoria': 'Adulto',
                    'posição': 'Armadora',
                    'codigo_cadastro': 20211042021202,
                    'país': 'França',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021105,
                    'nome': 'Kamilla Larsen',
                    'Idade': 38,
                    'id_time': 2021202,
                    'categoria': 'Adulto',
                    'posição': 'Pivo',
                    'codigo_cadastro': 20211052021202,
                    'país': 'Dinamarca',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021106,
                    'nome': 'Freja Cohrt',
                    'Idade': 27,
                    'id_time': 2021202,
                    'categoria': 'Adulto',
                    'posição': 'Ponta',
                    'codigo_cadastro': 20211062021202,
                    'país': 'Dinamarca',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021107,
                    'nome': 'Rikke Iversen',
                    'Idade': 28,
                    'id_time': 2021202,
                    'categoria': 'Adulto',
                    'posição': 'Pivo',
                    'codigo_cadastro': 20211072021202,
                    'país': 'Dinamarca',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021208,
                    'nome': 'Silvia Navarro',
                    'Idade': 42,
                    'id_time': 2021203,
                    'categoria': 'Adulto',
                    'posição': 'Goleira',
                    'codigo_cadastro': 20213082021203,
                    'país': 'Espanha',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021209,
                    'nome': 'Mizuki Hosoe',
                    'Idade': 28,
                    'id_time': 2021203,
                    'categoria': 'Adulto',
                    'posição': 'Central',
                    'codigo_cadastro': 20213092021203,
                    'país': 'Japao',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021210,
                    'nome': 'Agni Zygoura',
                    'Idade': 25,
                    'id_time': 2021203,
                    'categoria': 'Adulto',
                    'posição': 'Central',
                    'codigo_cadastro': 20213102021203,
                    'país': 'Grecia',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021211,
                    'nome': 'Rosana Martinez',
                    'Idade': 17,
                    'id_time': 2021203,
                    'categoria': 'Adulto',
                    'posição': 'Armadora',
                    'codigo_cadastro': 20213112021203,
                    'país': 'Espanha',
                    'Naipe': 'Feminino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021312,
                    'nome': 'Vicent Gerald',
                    'Idade': 34,
                    'id_time': 2021301,
                    'categoria': 'Adulto',
                    'posição': 'Goleiro',
                    'codigo_cadastro': 20214122021301,
                    'país': 'França',
                    'Naipe': 'Masculino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021313,
                    'nome': 'Leo Villain',
                    'Idade': 18,
                    'id_time': 2021301,
                    'categoria': 'Adulto',
                    'posição': 'Goleiro',
                    'codigo_cadastro': 20214132021301,
                    'país': 'França',
                    'Naipe': 'Masculino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021314,
                    'nome': 'Loik Spady',
                    'Idade': 21,
                    'id_time': 2021301,
                    'categoria': 'Adulto',
                    'posição': 'Goleiro',
                    'codigo_cadastro': 20214142021301,
                    'país': 'França',
                    'Naipe': 'Masculino',
                    'tipo': 'Profissional'
                },
                {
                    'id_atleta': 2021315,
                    'nome': 'Yann Genty',
                    'Idade': 39,
                    'id_time': 2021301,
                    'categoria': 'Adulto',
                    'posição': 'Goleiro',
                    'codigo_cadastro': 2021152021301,
                    'país': 'França',
                    'Naipe': 'Masculino',
                    'tipo': 'Profissional'
                }
            ]
        )
        insert_rows(
            cursor,
            'TIMES',
            [
                {
                    'id_time': 2021001,
                    'nome': 'Krim Mercator',
                    'id_tecnico': 20211,
                    'Naipe': 'Feminino',
                    'país': 'Eslovenia',
                    'tipo': 'Profissional',
                    'Competição_atual': 'EHF CHAMPIONS LEAGUE'

                },
                {
                    'id_time': 2021102,
                    'nome': 'Odense Handbold',
                    'id_tecnico': 20212,
                    'Naipe': 'Feminino',
                    'país': 'Dinamarca',
                    'tipo': 'Profissional',
                    'Competição_atual': 'EHF CHAMPIONS LEAGUE'
                },
                {
                    'id_time': 2021203,
                    'nome': 'Rocasa Gran Canaria',
                    'id_tecnico': 20213,
                    'Naipe': 'Feminino',
                    'país': 'Espanha',
                    'tipo': 'Profissional',
                    'Competição_atual': 'EHF EUROPEAN CUP'

                },
                {
                    'id_time': 2021301,
                    'nome': 'PARIS SANG GERMAIN Handball',
                    'id_tecnico': 202104,
                    'Naipe': 'Masculino',
                    'país': 'Dinamarca',
                    'tipo': 'Profissional',
                    'Competição_atual': 'EHF CHAMPIONS LEAGUE'
                },
                {
                    'id_time': 2021302,
                    'nome': 'RK Metaloplastika Sabac',
                    'id_tecnico': 202105,
                    'Naipe': 'Masculino',
                    'país': 'Servia',
                    'tipo': 'Profissional',
                    'Competição_atual': 'EHF EUROPEAN CUP'
                },
                {
                    'id_time': 2021303,
                    'nome': 'Herpertz Bevo HC',
                    'id_tecnico': 202106,
                    'Naipe': 'Masculino',
                    'país': 'Paises Baixos',
                    'tipo': 'Profissional',
                    'Competição_atual': 'EHF EUROPEAN CUP'
                },
            ]
        )
        insert_rows(
            cursor, #inserindo os dados da tabela de conexão
            'ATLETA_para_TIME',
            [
                {
                    'id_atleta': 2021001,
                    'id_time': 2021201
                },
                {
                    'id_atleta': 2021002,
                    'id_time': 2021201
                },
                {
                    'id_atleta': 2021003,
                    'id_time': 2021201
                },
                {
                    'id_atleta': 2021004,
                    'id_time': 2021202
                },
                {
                    'id_atleta': 2021105,
                    'id_time': 2021202
                },
                {
                    'id_atleta': 2021106,
                    'id_time': 2021202
                },
                {
                    'id_atleta': 2021107,
                    'id_time': 2021202
                },
                {
                    'id_atleta': 2021208,
                    'id_time': 2021203
                },
                {
                    'id_atleta': 2021209,
                    'id_time': 2021203
                },
                {
                    'id_atleta': 2021210,
                    'id_time': 2021203
                },
                {
                    'id_atleta': 2021211,
                    'id_time': 2021203
                },
                {
                    'id_atleta': 2021312,
                    'id_time': 2021301
                },
                {
                    'id_atleta': 2021313,
                    'id_time': 2021301
                },
                {
                    'id_atleta': 2021314,
                    'id_time': 2021301
                },
                {
                    'id_atleta': 2021315,
                    'id_time': 2021301
                },
            ]
        )
        insert_rows( #Inserindo os dados da tabela de conexão
            cursor,
            'TECNICO_para_TIME',
            [
                {
                    'id_tecnico': 20211,
                    'id_time': 2021001
                },
                {
                    'id_tecnico': 20212,
                    'id_time': 2021102
                },
                {
                    'id_tecnico': 20213,
                    'id_time': 2021203
                },
                {
                    'id_tecnico': 202104,
                    'id_time': 2021301
                },
                {
                    'id_tecnico': 202105,
                    'id_time': 2021302
                },
                {
                    'id_tecnico': 202106,
                    'id_time': 2021303
                },
            ]
        )


if __name__ == '__main__':
    main()