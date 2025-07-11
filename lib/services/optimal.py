""""""

class OptimalMetadata:
    def __init__(self, problem_id: str, solver: str, sense: str):
        self.problem_id = problem_id
        self.solver = solver
        self.sense = sense

    def to_dict(self):
        return {
            "problem_id": self.problem_id,
            "solver": self.solver,
            "sense": self.sense
        }


class OptimalSchema:
    def __init__(self, meta: OptimalMetadata, variables: list, parameters: dict, objective: dict, constraints: list, initial_guess: list):
        self.meta = meta
        self.variables = variables
        self.parameters = parameters
        self.objective = objective
        self.constraints = constraints
        self.initial_guess = initial_guess

    def to_dict(self):
        return {
            "meta": self.meta.to_dict(),
            "variables": self.variables,
            "parameters": self.parameters,
            "objective": self.objective,
            "constraints": self.constraints,
            "initial_guess": self.initial_guess
        }

class OptimalService:
    def __init__(self, url: str, api_key: str, schema: OptimalSchema):
        self.url = url
        self.api_key = api_key
        self.schema = schema

    @property
    def payload(self) -> dict:
        return self.schema.to_dict()

    @property
    def headers(self):
        if not self.api_key:
            raise ValueError("API key is required for OptimalService")

        return {
            'x-api-key': self.api_key
        }

    def send(self):
        import requests

        resp = requests.post(
            "https://optimal.apphosting.services/optimize",
            json=self.payload,
            headers=self.headers,
            timeout=30
        )

        print(resp.status_code, resp.text)

        if resp.status_code != 200:
            raise Exception(f"Optimal service error: {resp.status_code} - {resp.text}")

        return resp.json()
