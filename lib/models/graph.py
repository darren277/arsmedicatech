""""""
from lib.db.surreal import DbController
from lib.db.surreal_graph import GraphController
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


graph_db = GraphController(db)



""" NODES """

def create_node(node_type: str, node_id: str, node_name: str, **fields):
    db.create(f'{node_type}:{node_id}', dict(name=node_name, **fields))

def query_node(node_type: str, node_id: str):
    return db.query(f"SELECT * FROM {node_type}:{node_id}")




# -- Create some symptoms
# CREATE symptom:loss_of_appetite SET name = "Loss of appetite";
# CREATE symptom:fatigue          SET name = "Fatigue";

create_node('symptom', 'loss_of_appetite', 'Loss of appetite')
create_node('symptom', 'fatigue', 'Fatigue')


# -- Create some diagnoses
# CREATE diagnosis:depression SET name = "Depression";
# CREATE diagnosis:flu        SET name = "Influenza (Flu)";

create_node('diagnosis', 'depression', 'Depression')
create_node('diagnosis', 'flu', 'Influenza (Flu)')


# -- Create some medications
# CREATE medication:prozac    SET name = "Prozac";
# CREATE medication:ibuprofen SET name = "Ibuprofen";
# CREATE medication:warfarin  SET name = "Warfarin";

create_node('medication', 'prozac', 'Prozac')
create_node('medication', 'ibuprofen', 'Ibuprofen')
create_node('medication', 'warfarin', 'Warfarin')



# Query a single node (just to verify that it exists - or to get its attributes)

# SELECT * FROM symptom:loss_of_appetite
symptom = query_node('symptom', 'loss_of_appetite')
print(symptom)




""" EDGES """

# RELATE <record> -> <edge_name> -> <record> SET <fields>;


''' A. Diagnosis -> HAS_SYMPTOM -> Symptom '''

graph_db.relate(
    'diagnosis:depression',
    'HAS_SYMPTOM',
    'symptom:loss_of_appetite',
    dict(note='Common symptom in depression')
)

graph_db.relate(
    'diagnosis:depression',
    'HAS_SYMPTOM',
    'symptom:fatigue',
    dict(note='Patients often report feeling very tired')
)

graph_db.relate(
    'diagnosis:flu',
    'HAS_SYMPTOM',
    'symptom:fatigue',
    dict(note='Fatigue is frequently reported in flu')
)


# Get outgoing connections (symptoms of depression)
# SELECT ->HAS_SYMPTOM->symptom FROM diagnosis:depression
symptoms = graph_db.get_relations('diagnosis:depression', 'HAS_SYMPTOM', 'symptom')
print(symptoms)


# Get incoming connections (diagnoses that have loss of appetite)
# SELECT <-HAS_SYMPTOM-<diagnosis FROM symptom:loss_of_appetite
diagnoses = graph_db.get_relations('symptom:loss_of_appetite', 'HAS_SYMPTOM', 'diagnosis', direction='<-')
print(diagnoses)


# Query a single edge (just to verify that it exists - or to get its attributes)

# SELECT * FROM ->HAS_SYMPTOM->symptom:loss_of_appetite
def query_edges(from_node: str, from_id: str, edge_name: str):
    return db.query(f'SELECT ->{edge_name}.* FROM {from_node}:{from_id}')[0]

edge = query_edges('diagnosis', 'depression', 'HAS_SYMPTOM')



''' B. Medication -> TREATS -> Diagnosis '''

graph_db.relate(
    'medication:prozac',
    'TREATS',
    'diagnosis:depression',
    dict(note='Used for major depressive disorder')
)

graph_db.relate(
    'medication:ibuprofen',
    'TREATS',
    'diagnosis:flu',
    dict(note='Helps reduce fever and pain')
)



''' C. Symptom -> CONTRAINDICATED_FOR -> Medication '''

graph_db.relate(
    'symptom:fatigue',
    'CONTRAINDICATED_FOR',
    'medication:prozac',
    dict(reason='Prozac can worsen sedation in some patients (example)')
)

graph_db.relate(
    'symptom:fatigue',
    'CONTRAINDICATED_FOR',
    'medication:warfarin',
    dict(reason='Increases risk of bleeding when taken concurrently.')
)



''' D. Medication -> CONTRAINDICATED_FOR -> Medication '''

graph_db.relate(
    'medication:warfarin',
    'CONTRAINDICATED_FOR',
    'medication:ibuprofen',
    dict(reason='Increases risk of bleeding when taken concurrently.')
)


