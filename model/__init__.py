import os
import sqlite3


class SQLite(object):
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


def create_table(cursor: sqlite3.Cursor, table: str, fields: dict, other_data: list = None) -> None:
    """
    Função para criar tabelas.

    :param cursor: um cursor para o banco de dados
    :param table: Nome da tabela
    :param fields: Um dicionário onde a chave é o nome da coluna, e o valor o tipo/modificadores (e.g. primary key)
    :param other_data: Para definir foreign keys, ou outras configurações.
    """
    command = "CREATE TABLE %s (%s)" % (
        table,
        ','.join([k + ' ' + v for k, v in fields.items()] + (
            other_data if other_data is not None else []))
    )
    cursor.execute(command)


def insert_rows(cursor: sqlite3.Cursor, table: str, tuples: list) -> None:
    """
    Função para inserir tuplas numa tabela.

    :param cursor: um cursor para o banco de dados
    :param table: Nome da tabela
    :param tuples: Uma lista de dicionários. Para cada dicionário, a chave é o nome da coluna, e o valor, o valor da tupla
    para aquela coluna.
    """
    for some_tuple in tuples:
        tuple_values = []
        for v in some_tuple.values():
            if isinstance(v, str):
                tuple_values += ['\'' + v + '\'']
            else:
                tuple_values += [str(v)]

        command = "INSERT INTO %s(%s) VALUES (%s)" % (
            table, ','.join(map(str, some_tuple.keys())), ','.join(tuple_values)
        )
        cursor.execute(command)


def select_rows(cursor: sqlite3.Cursor, clause: str) -> list:
    """
    Método para fazer seleção de tuplas de uma tabela. Aceita qualquer comando SQLITE.

    :param cursor: um cursor para o banco de dados
    :param clause: A cláusula de seleção (e.g. SELECT * FROM table)
    :return: Uma lista de tuplas
    """
    res = cursor.execute(clause)
    rows = []
    for row in res:  # type: sqlite3.Row
        rows += [tuple([row[k] for k in row.keys()])]

    return rows


def raw_execute(cursor: sqlite3.Cursor, clause: str) -> sqlite3.Cursor:
    """
    Executa qualquer comando SQLITE. Retorna o resultado.

    :param cursor: um cursor para o banco de dados
    :param clause: Qualquer cláusula SQLITE.
    :return: O resultado da execução da cláusula (se ela retorna um valor), ou None.
    """
    return cursor.execute(clause)


def remove_db(file: str) -> None:
    """
    Deleta o arquivo .db contido em file.

    :param file: Caminho para o banco .db.
    """
    try:
        os.remove(file)
    except FileNotFoundError:
        pass


def main(path: str = '.', db_name: str = 'test.db') -> None:
    remove_db(os.path.join(path, db_name))

    with SQLite(os.path.join(path, db_name)) as cursor:
        # TODO desenvolva seu código aqui
        create_table(
            cursor,
            'memes',
            {'id': 'INTEGER PRIMARY KEY', 'nome': 'text NOT NULL', 'link': 'text NOT NULL', 'ranking': 'INTEGER NULL'}
        )
        create_table(
            cursor,
            'usuarios',
            {'id': 'INTEGER PRIMARY KEY', 'nome': 'text NOT NULL'}
        )
        create_table(
            cursor,
            'usuarios_para_memes',
            {'id_meme': 'INTEGER NOT NULL', 'id_usuario': 'INTEGER NOT NULL'},
            ['PRIMARY KEY(id_meme, id_usuario)', 'FOREIGN KEY(id_meme) REFERENCES memes(id)',
             'FOREIGN KEY(id_usuario) REFERENCES usuarios(id)']
        )

        insert_rows(
            cursor,
            'memes',
            [
                {
                    'id': 1,
                    'nome': 'DJ André Marques manda AQUELE ao vivo',
                    'link': 'https://www.youtube.com/watch?v=zObCCCsCo2I',
                    'ranking': 1
                },
                {
                    'id': 2,
                    'nome': '10 mandamentos rei do camarote',
                    'link': 'https://www.youtube.com/watch?v=atQvZ-nq0Go',
                    'ranking': 5
                },
            ]
        )
        insert_rows(
            cursor,
            'usuarios',
            [{'id': 1, 'nome': 'henry'}]
        )
        insert_rows(
            cursor,
            'usuarios_para_memes',
            [
                {'id_meme': 1, 'id_usuario': 1},
                {'id_meme': 2, 'id_usuario': 1}
            ]
        )
        rows = select_rows(
            cursor,
            "SELECT usuarios.nome AS nome_usuario, memes.nome AS nome_meme "
            "FROM memes "
            "INNER JOIN usuarios_para_memes ON memes.id=usuarios_para_memes.id_meme "
            "INNER JOIN usuarios ON usuarios.id=usuarios_para_memes.id_usuario;")
        print(rows)
        # TODO desenvolva seu código aqui


if __name__ == '__main__':
    main()
