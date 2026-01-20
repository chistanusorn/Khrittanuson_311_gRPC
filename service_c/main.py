import threading
import uvicorn
from fastapi import FastAPI
from grpc_server import serve
from fastapi.responses import FileResponse

app = FastAPI()

def start_grpc():
    serve()

@app.get("/download-decree")
def download_file():
    # ส่งไฟล์ที่อยู่ในโฟลเดอร์ออกมาให้ User ดาวน์โหลด
    file_path = "holy_decree.pdf"
    return FileResponse(path=file_path, filename="Divine_Decree.pdf", media_type='application/pdf')

if __name__ == "__main__":
    t = threading.Thread(target=start_grpc, daemon=True)
    t.start()
    uvicorn.run(app, host="0.0.0.0", port=8002) # HTTP Port 8002