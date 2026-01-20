import threading # สำหรับรัน gRPC แยกไปอีกหน้าต่างหนึ่ง (Thread)
import uvicorn # เครื่องมือสำหรับรัน FastAPI
from fastapi import FastAPI # นำเข้าตัวจัดการ API
from grpc_server import serve # นำเข้าฟังก์ชันรัน gRPC ที่เราเขียนไว้ข้างบน

app = FastAPI(title="Service A - User Information Service")

@app.get("/")
def read_root():
    # หน้าแรกสำหรับตรวจสอบว่า Service ยังทำงานอยู่ไหม
    return {"status": "Service A (User) is running peacefully ❤︎"}

def start_grpc_server():
    # เรียกใช้ฟังก์ชัน serve เพื่อรัน gRPC
    serve()

if __name__ == "__main__":
    # รัน gRPC Server ใน Background Thread เพื่อไม่ให้ไปขัดขวาง FastAPI
    grpc_thread = threading.Thread(target=start_grpc_server, daemon=True)
    grpc_thread.start()
    
    # รัน FastAPI บนพอร์ต 8000 (ใช้ 0.0.0.0 เพื่อให้ Docker คุยกันรู้เรื่อง)
    uvicorn.run(app, host="0.0.0.0", port=8000)