Install the dependencies:

`pipenv install`

Start the database with docker:

`pipenv run start_postgres`

Run the server:

`pipenv run runserver`

Run the worker:

`pipenv run runworker`

connect with a websocket client:

`npx wscat -c ws://localhost:8002/ws/test/`

Send any message to the worker
