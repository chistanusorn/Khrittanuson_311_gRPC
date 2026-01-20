import threading
import uvicorn
from fastapi import FastAPI
from grpc_server import serve

app = FastAPI()

def start_grpc():
    serve()

if __name__ == "__main__":
    t = threading.Thread(target=start_grpc, daemon=True)
    t.start()
    uvicorn.run(app, host="0.0.0.0", port=8002) # HTTP Port 8002