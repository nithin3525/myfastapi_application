from fastapi import FastAPI

app = FastAPI()

@app.get("/admin")
def admin():
    return "hello admin!"

