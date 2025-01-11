""""""
from surrealdb import SurrealDB

from settings import *


class DbController:
    def __init__(self, url=SURREALDB_URL, namespace=SURREALDB_NAMESPACE, database=SURREALDB_DATABASE, user=SURREALDB_USER, password=SURREALDB_PASS):
        self.db = SurrealDB(url)
        self.namespace = namespace
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        self.db.connect()
        self.db.use(self.namespace, self.database)
        self.db.sign_in(self.user, self.password)

    def query(self, statement: str, params = None):
        #print("QUERY", statement, params)
        if not params: return self.db.query(statement)
        else: return self.db.query(statement, params)

    def update(self, record, data):
        print(record, data)
        result = self.db.update(record, data)
        _id = f'{result.pop("id")}'
        self.db.close()
        return dict(**result, id=_id)

    def create(self, table_name, data):
        try:
            result = self.db.create(table_name, data)
        except Exception as e:
            print("ERROR", e)
            result = dict()
        # {'id': RecordID(table_name=mytable, record_id=l3s7faxhjm8tsn6lecu9), 'name': 'John Doe'}
        _id = f'{result.pop("id")}'
        self.db.close()
        return dict(**result, id=_id)

    def select_many(self, table_name):
        result = self.db.select(table_name)
        for i, record in enumerate(result):
            _id = f'{record.pop("id")}'
            result[i] = dict(**record, id=_id)
        self.db.close()
        return result

    def select(self, record):
        result = self.db.select(record)
        _id = f'{result.pop("id")}'
        self.db.close()
        return dict(**result, id=_id)

    def delete(self, record):
        result = self.db.delete(record)
        self.db.close()
        return result

    def close(self):
        self.db.close()
