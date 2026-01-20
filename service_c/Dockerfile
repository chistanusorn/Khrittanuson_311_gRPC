# ใช้ Python version ที่เสถียร
FROM python:3.10-slim

# ตั้งค่าโฟลเดอร์ทำงานใน Container
WORKDIR /app

# คัดลอกไฟล์ requirements และติดตั้ง Library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดลงไป
COPY . .

# รันคำสั่งแปลงไฟล์ Proto เป็น Python Code (เพื่อให้แน่ใจว่าใช้งานได้)
# หมายเหตุ: ในแต่ละ service ชื่อไฟล์ .proto จะต่างกัน ท่านต้องแก้ให้ตรงนะคะ
# ตัวอย่างสำหรับ Service A:
# RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/user.proto

# คำสั่งเริ่มต้นทำงาน
CMD ["python", "main.py"]