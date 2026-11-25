from fastapi import FastAPI


import uvicorn
import os


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", port=7979, log_level="info", reload=True)