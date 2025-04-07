""""""
from lib.db.surreal import DbController
from settings import SURREALDB_URL, SURREALDB_NAMESPACE, SURREALDB_USER, SURREALDB_PASS

'''
[AMT-011]: Graph Schema for SurrealDB

Our first graph schema for our application will be a medical knowledge graph of the following relations: `symptoms ↔ diagnoses ↔ treatments ↔ medications ↔ side effects`.

Model
-----

Nodes:
* Symptom.
* Diagnosis.
* Medication.

Edges:
* Diagnosis => `HAS_SYMPTOM` => Symptom.
* Medication => `TREATS` => Diagnosis.
* Symptom => `CONTRAINDICATED_FOR` => Medication.
* Medication => `CONTRAINDICATED_FOR` => Medication.

That will be our starting point at least and we can expand on it later.
'''

db = DbController(url=SURREALDB_URL, namespace=SURREALDB_NAMESPACE, database='graph', user=SURREALDB_USER, password=SURREALDB_PASS)
db.connect()

def create_node(node_type: str, node_id: str, node_name: str, **fields):
    db.create(f'{node_type}:{node_id}', dict(name=node_name, **fields))

create_node('symptom', 'loss_of_appetite', 'Loss of appetite')
create_node('symptom', 'fatigue', 'Fatigue')
