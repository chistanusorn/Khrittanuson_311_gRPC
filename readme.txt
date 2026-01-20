คริสตนุสรณ์ มหาวีระตระกูล 311
--------------------------------------------------
1. อธิบายการทำงาน:
- โปรเจคนี้เป็นระบบ Microservices 3 ตัวที่ทำงานร่วมกัน
- Service B ทำหน้าที่เป็น Gateway รับ REST Request จากผู้ใช้
- Service B สื่อสารกับ Service A (User) และ Service C (Order) ผ่าน gRPC
- ข้อมูลถูกรวบรวม (Aggregation) และส่งกลับในรูปแบบ Direct Mapping

2. รายละเอียดการ Request/Response:
- Client -> (REST GET) -> Service B
- Service B -> (gRPC Request) -> Service A [รับข้อมูลชื่อผู้ใช้]
- Service B -> (gRPC Request) -> Service C [รับข้อมูลรายการสินค้า]
- Service B -> (JSON Response) -> Client

3. วิธีการรัน:
- ติดตั้ง Docker และ Docker Compose
- เปิด Terminal ในโฟลเดอร์หลัก
- รันคำสั่ง: docker-compose up --build
- เข้าไปที่ http://localhost:8001/dashboard ผ่าน Browser จะพบหน้า dashboard ที่สวยงาม **แนะนำให้เข้าไปที่หน้านี้**
- เข้าไปที่ http://localhost:8001/saints-profile ผ่าน Browser
- หรือเข้าไปที่ http//localhost:8001/docs

4. ผลลัพธ์ที่ควรได้:
- จะเห็นข้อมูล JSON ที่รวมชื่อของ Philia และ Mia พร้อมรายการไอเทมศักดิ์สิทธิ์

Project Tree
grpc-microservice-project/
├── proto/                      # เก็บไฟล์ต้นฉบับ Protocol Buffers 
│   └── user.proto              # กำหนด Service และ Message schema
├── generated/                  # ไฟล์ Python ที่ถูก Generate ออกมา 
│   ├── __init__.py
│   ├── user_pb2.py            # Message classes
│   └── user_pb2_grpc.py       # Server/Client stubs
├── app/                        # Source Code หลักของ Application
│   ├── __init__.py
│   ├── main.py                # FastAPI (Gateway) ที่เรียกใช้ gRPC client
│   ├── grpc_server.py         # gRPC Server implementation (Business Logic หลัก)
│   └── grpc_client.py         # Script สำหรับทดสอบเชื่อมต่อ gRPC
├── requirements.txt            # รายชื่อ Libraries (fastapi, grpcio, etc.)
└── README.md                   # เอกสารอธิบายโปรเจกต์
