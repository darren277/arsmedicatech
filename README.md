# ArsMedicaTech

## About

TBD...

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
