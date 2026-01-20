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
- เข้าไปที่ http://localhost:8001/saints-profile ผ่าน Browser
- หรือเข้าไปที่ http//localhost:8001/docs

4. ผลลัพธ์ที่ควรได้:
- จะเห็นข้อมูล JSON ที่รวมชื่อของ Philia และ Mia พร้อมรายการไอเทมศักดิ์สิทธิ์