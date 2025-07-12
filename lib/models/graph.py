"""
Graph Schema for SurrealDB
"""
from typing import Any, Dict, List

from lib.db.surreal import DbController
from lib.db.surreal_graph import GraphController
from settings import (SURREALDB_NAMESPACE, SURREALDB_PASS, SURREALDB_URL,
                      SURREALDB_USER, logger)

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

def create_node(node_type: str, node_id: str, node_name: str, **fields: Dict[str, Any]) -> None:
    """
    Create a node in the graph database.
    :param node_type: str - Type of the node (e.g., 'symptom', 'diagnosis', 'medication').
    :param node_id: str - Unique identifier for the node.
    :param node_name: str - Name of the node.
    :param fields: dict - Additional fields to set on the node.
    :return: None
    """
    db.create(f'{node_type}:{node_id}', dict(name=node_name, **fields))

def query_node(node_type: str, node_id: str) -> List[Dict[str, Any]]:
    """
    Query a single node in the graph database.
    :param node_type: str - Type of the node (e.g., 'symptom', 'diagnosis', 'medication').
    :param node_id: str - Unique identifier for the node.
    :return: dict - The node record from the database.
    """
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
logger.debug(str(symptom))




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
logger.debug(symptoms)


# Get incoming connections (diagnoses that have loss of appetite)
# SELECT <-HAS_SYMPTOM-<diagnosis FROM symptom:loss_of_appetite
diagnoses = graph_db.get_relations('symptom:loss_of_appetite', 'HAS_SYMPTOM', 'diagnosis', direction='<-')
logger.debug(diagnoses)


# Query a single edge (just to verify that it exists - or to get its attributes)

# SELECT * FROM ->HAS_SYMPTOM->symptom:loss_of_appetite
def query_edges(from_node: str, from_id: str, edge_name: str) -> Dict[str, Any]:
    """
    Query a single edge in the graph database.
    :param from_node: str - Type of the node (e.g., 'diagnosis', 'symptom').
    :param from_id: str - Unique identifier for the node.
    :param edge_name: str - Name of the edge (e.g., 'HAS_SYMPTOM').
    :return: dict - The edge record from the database.
    """
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

graph_db.relate(
    'medication:warfarin',
    'CONTRAINDICATED_FOR',
    'medication:prozac',
    dict(reason='Increases risk of bleeding when taken concurrently.')
)




# -- List all diagnoses and see their edges:
# SELECT * FROM diagnosis;

diagnoses = db.query('SELECT * FROM diagnosis')

for diagnosis in diagnoses:
    logger.debug(str(diagnosis))
    # Get outgoing connections (symptoms of depression)
    symptoms = graph_db.get_relations(diagnosis['id'], 'HAS_SYMPTOM', 'symptom')
    logger.debug(symptoms)


# -- For a specific diagnosis, find its related symptoms:
# SELECT ->HAS_SYMPTOM.* FROM diagnosis:depression;

depression_symptoms_result = db.query('SELECT ->HAS_SYMPTOM.* FROM diagnosis:depression')
depression_symptoms = depression_symptoms_result[0]['->HAS_SYMPTOM']
logger.debug(depression_symptoms)

for symptom in depression_symptoms:
    # symptom: dict_keys(['id', 'in', 'note', 'out'])
    logger.debug(f"Symptom: {symptom['id']}. Note: {symptom['note']}. In: {symptom['in']}. Out: {symptom['out']}")


# -- For a medication, see which diagnoses it treats and what it might be contraindicated for:
# SELECT ->TREATS.* FROM medication:prozac;
# SELECT ->CONTRAINDICATED_FOR.* FROM medication:warfarin;

prozac_diagnoses = db.query('SELECT ->TREATS.* FROM medication:prozac')
prozac_diagnoses = prozac_diagnoses[0]['->TREATS']
logger.debug(prozac_diagnoses)


for diagnosis in prozac_diagnoses:
    # Get incoming connections (medications that are contraindicated for Prozac)

    direction = '<-'
    medications = graph_db.get_relations('medication:prozac', 'CONTRAINDICATED_FOR', 'medication', direction=direction)
    medications = medications[0]['<-CONTRAINDICATED_FOR']['<-medication']
    for medication in medications:
        logger.debug(medication)

    direction = '->'
    medications = graph_db.get_relations('medication:prozac', 'CONTRAINDICATED_FOR', 'medication', direction=direction)
    medications = medications[0]['->CONTRAINDICATED_FOR']['->medication']
    for medication in medications:
        logger.debug(medication)


