# Running Locally

The goal of this readme doc is to provide the bare essentials for getting the app running locally.

First, a brief overview of the architecture:
1. There is a Flask app that servers the backend API.
2. There is a React app that serves the frontend.
3. SurrealDB is used for the database.

There are also the following components that may not be required for all local development:
1. A Flask MCP server for LLM tool calling.
2. Redis for notification pubsub.

As for environment variables, I provide an example in `.env.example`. You can copy this file to `.env` and modify it as needed.

Note that it only contains the essentials.

Some API keys are not included if they are not essential to all features.

There are also some environment variables specifically for deployments (to Kubernetes).

## Steps

1. Initialize a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```
3. Start the SurrealDB server using Docker:
   ```bash
    docker run -d --name surrealdb -p 8000:8000 surrealdb/surrealdb:latest start --user root --pass root memory
   ```
4. Start the Flask app:
   ```bash
    python app.py
   ```
5. Start the React app:
   ```bash
    cd frontend
    npm install
    npm start
   ```
6. Open your browser and navigate to `http://localhost:3000` to access the app.
7. If you want to run the MCP server for LLM tool calling, you can do so with:
   ```bash
    python mcp_server.py
   ```
8. If you want to run the Redis server for notifications, you can do so with:
   ```bash
    redis-server
   ```

If any of the above steps do not work, please let me know and I will adjust them accordingly!
