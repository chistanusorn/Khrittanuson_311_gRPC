import grpc # นำเข้าไลบรารี gRPC
from concurrent import futures # สำหรับจัดการ Threading ให้เซิร์ฟเวอร์รองรับหลาย Request
import user_pb2 # ไฟล์ที่ Generate มาจาก .proto (บรรจุโครงสร้างข้อมูล)
import user_pb2_grpc # ไฟล์ที่ Generate มาจาก .proto (บรรจุโครงสร้าง Service)

# จำลองฐานข้อมูลผู้ใช้ (Mock Database) 
USER_DB = {
    1: {"user_name": "Philia Adenauer", "email": "philia.saint@kingdom.com", "is_active": True},
    2: {"user_name": "Mia Adenauer", "email": "mia.saint@kingdom.com", "is_active": True},
}

# สร้าง Class สำหรับจัดการคำขอที่ส่งมาหา UserService
class UserServiceServicer(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        """
        ฟังก์ชันนี้จะทำงานเมื่อมีการเรียกใช้ RPC 'GetUser'
        - request.user_id: คือ ID ที่ฝั่ง Client ส่งมา
        """
        user_id = request.user_id
        user = USER_DB.get(user_id) # ค้นหาข้อมูลใน Mock DB
        
        if user:
            # หากเจอข้อมูล ให้ส่ง UserReply กลับไปตามโครงสร้างที่กำหนดใน .proto
            return user_pb2.UserReply(
                user_name=user["user_name"],
                email=user["email"],
                is_active=user["is_active"]
            )
        else:
            # หากไม่เจอ ให้ส่งกลับแบบว่างเปล่า (หรือจะตั้งค่า Error ก็ได้)
            return user_pb2.UserReply()

def serve():
    """ฟังก์ชันหลักสำหรับเริ่มรัน gRPC Server"""
    # สร้าง gRPC Server โดยใช้ ThreadPool ขนาด 10
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # ลงทะเบียน Service เข้ากับ Server
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    # กำหนดพอร์ตในการรับฟังคำขอ (Insecure คือไม่ใช้ SSL ในแล็บนี้)
    server.add_insecure_port('[::]:50051')
    print("Starting User gRPC server on port 50051...")
    server.start() # เริ่มการทำงาน
    server.wait_for_termination() # รันค้างไว้จนกว่าจะมีการปิดโปรแกรม