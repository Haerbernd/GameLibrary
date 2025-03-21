from fastapi import FastAPI


app: FastAPI = FastAPI()
HOST: str = "127.0.0.1"
PORT: int = 8000


@app.get("/")
def root() -> dict:
    return {"path": "root", "connection_successful": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
