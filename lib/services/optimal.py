"""
Optimal Service Module

Optimal is an API for solving optimization problems using various solvers.
"""
from typing import Any, Dict, List

from settings import logger


class OptimalMetadata:
    """
    Metadata for the optimization problem.
    """
    def __init__(self, problem_id: str, solver: str, sense: str) -> None:
        """
        Initializes the metadata for the optimization problem.
        :param problem_id: The unique identifier for the optimization problem.
        :param solver: The solver to be used for the optimization problem.
        :param sense: The sense of the optimization problem, e.g., 'minimize' or 'maximize'.
        """
        self.problem_id = problem_id
        self.solver = solver
        self.sense = sense

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the metadata to a dictionary format.
        :return: dict: A dictionary representation of the metadata.
        """
        return {
            "problem_id": self.problem_id,
            "solver": self.solver,
            "sense": self.sense
        }


class OptimalSchema:
    """
    Schema for the optimization problem to be sent to the Optimal service.
    """
    def __init__(
            self,
            meta: OptimalMetadata,
            variables: List[str],
            parameters: Dict[str, Any],
            objective: Dict[str, Any],
            constraints: List[Dict[str, Any]],
            initial_guess: List[float]
        ) -> None:
        """
        Initializes the schema for the optimization problem.
        :param meta: OptimalMetadata: Metadata for the optimization problem.
        :param variables: list: List of variables in the optimization problem.
        :param parameters: dict: Dictionary of parameters for the optimization problem.
        :param objective: dict: The objective function for the optimization problem.
        :param constraints: list: List of constraints for the optimization problem.
        :param initial_guess: list: Initial guess for the optimization variables.
        :return: None
        """
        self.meta = meta
        self.variables = variables
        self.parameters = parameters
        self.objective = objective
        self.constraints = constraints
        self.initial_guess = initial_guess

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the schema to a dictionary format.
        :return: dict: A dictionary representation of the optimization schema.
        """
        return {
            "meta": self.meta.to_dict(),
            "variables": self.variables,
            "parameters": self.parameters,
            "objective": self.objective,
            "constraints": self.constraints,
            "initial_guess": self.initial_guess
        }

class OptimalService:
    """
    Service for interacting with the Optimal API to solve optimization problems.
    """
    def __init__(self, url: str, api_key: str, schema: OptimalSchema) -> None:
        """
        Initializes the OptimalService with the required parameters.
        :param url: The URL of the Optimal service endpoint.
        :param api_key: The API key for authenticating with the Optimal service.
        :param schema: OptimalSchema: The schema representing the optimization problem.
        :return: None
        """
        self.url = url
        self.api_key = api_key
        self.schema = schema

    @property
    def payload(self) -> Dict[str, Any]:
        """
        Constructs the payload to be sent to the Optimal service.
        :return: dict: The payload containing the schema and metadata.
        """
        return self.schema.to_dict()

    @property
    def headers(self) -> Dict[str, str]:
        """
        Constructs the headers for the HTTP request to the Optimal service.
        :raises ValueError: If the API key is not provided.
        :return: dict: The headers including the API key for authentication.
        """
        if not self.api_key:
            raise ValueError("API key is required for OptimalService")

        return {
            'x-api-key': self.api_key
        }

    def send(self) -> Dict[str, Any]:
        """
        Sends the optimization problem to the Optimal service and returns the response.
        :return: dict: The response from the Optimal service containing the optimization results.
        """
        import requests

        resp = requests.post(
            "https://optimal.apphosting.services/optimize",
            json=self.payload,
            headers=self.headers,
            timeout=30
        )

        logger.debug(f"Status code: {resp.status_code}, Response text: {resp.text}")

        if resp.status_code != 200:
            raise Exception(f"Optimal service error: {resp.status_code} - {resp.text}")

        return resp.json()
