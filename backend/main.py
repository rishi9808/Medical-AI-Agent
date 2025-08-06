# set up FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from uvicorn import run

#  initialize FastAPI app
app = FastAPI()

# define a model for the query (for validation of input)
class Query(BaseModel):
    message: str

# define a route to handle queries
@app.post("/query")
async def handle_query(query: Query):
    # Here you would typically process the query.message
    # and return a response. For now, we'll just echo the message.
    return {"message": f"Received: {query.message}"}


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000, log_level="info")

