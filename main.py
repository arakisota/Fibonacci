# main.py
from fastapi import FastAPI, HTTPException
from fibonacci import fibonacci

app = FastAPI()


@app.get("/fib")
async def get_fibonacci(n: int):
    try:
        result = fibonacci(n)
        return {"result": result}
    except HTTPException as e:
        return {"status": e.status_code, "message": e.detail}
