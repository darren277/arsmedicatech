# ArsMedicaTech

## About

This is a broad purpose web application for various kinds of clinical use cases. It has a Flask server, a React front end, SurrealDB for a multimodel database, LLM integration, OSCAR EMR integration, and much, much more.

## How to Use

TBD...

### Webpack devServer vs Webpack build vs No Webpack...?

`webpack serve --config ./webpack.config.js --mode development --port 3010`

vs...

`npm start ./src/index.js`

`npm start ./src/index.js --port=3010 --proxy=http://127.0.0.1:5010`

## Databases

### SurrealDB

#### ICD

Example: `section111validicd10-jan2025_0.csv`:
```csv
CODE,SHORT DESCRIPTION (VALID ICD-10 FY2025),LONG DESCRIPTION (VALID ICD-10 FY2025)
A000,"Cholera due to Vibrio cholerae 01, biovar cholerae","Cholera due to Vibrio cholerae 01, biovar cholerae"
A001,"Cholera due to Vibrio cholerae 01, biovar eltor","Cholera due to Vibrio cholerae 01, biovar eltor"
A009,"Cholera, unspecified","Cholera, unspecified"
A0100,"Typhoid fever, unspecified","Typhoid fever, unspecified"
A0101,Typhoid meningitis,Typhoid meningitis
```

#### Graph

We have added a graph database to our ecosystem.

For now, it just has some basic example nodes and relationships such as:
* `Diagnosis` -> `HAS_SYMPTOM` -> `Symptom`.
* `Medication` -> `TREATS` -> `Diagnosis`.
* `Symptom` -> `CONTRAINDICATED_FOR` -> `Medication`.
* `Medication` => `CONTRAINDICATED_FOR` => `Medication`.

Admittedly, it took me some time to start wrapping my head around the querying syntax for relationships, so I did not explore them as far as I would have liked to this time around.

I definitely plan on tackling some more complex use cases in the future as there is a lot of potential for that with graph databases.

Another caveat is that, currently as of this writing, a lot of the queries are a mix of standalone functions and use of our dedicated wrapper controller I started building out. I'd of course like that to be more consistent, but will return to that in the future.

##### Some Possible Future Direction to Explore

Add More Fields: You can store additional fields (e.g., `icd_code`, `description`, `severity`) on both node records and edge records.

Schema Definitions (Optional): SurrealDB allows schema definitions (`SCHEMAFULL`, `SCHEMALESS`) to enforce constraints if you want more structure.

Additional Node Types: Over time, you might add `Treatment` or `Procedure` nodes, or even `SideEffect` nodes.

Complex Edges: You could represent more nuanced relationships (e.g., “alleviates symptom,” “risk factor for,” “co-morbidity with,” etc.).

Integration with External Data: To fill out a large knowledge graph, you can look into open data sources:
* ICD-10/11 codes (WHO)
* UMLS Metathesaurus (NIH)
* SNOMED CT
