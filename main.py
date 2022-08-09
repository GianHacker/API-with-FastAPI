from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def greetingMessage():
    return "Hi, Let's Learn API using Python & fastapi framework"
