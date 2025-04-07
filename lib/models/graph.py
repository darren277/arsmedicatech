""""""

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
