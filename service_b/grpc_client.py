import os
import grpc
import user_pb2
import user_pb2_grpc
import order_pb2
import order_pb2_grpc

# กำหนดชื่อ Host สำหรับติดต่อภายใน Docker (ถ้าไม่ได้รันใน Docker จะใช้ localhost แทน)
USER_HOST = os.getenv("USER_SERVICE_HOST", "service_a")
ORDER_HOST = os.getenv("ORDER_SERVICE_HOST", "service_c")

def get_user_info(user_id: int):
    """ฟังก์ชันดึงข้อมูลผู้ใช้จาก Service A ผ่าน gRPC"""
    # เชื่อมต่อไปยัง Service A ตาม Port ที่กำหนด
    with grpc.insecure_channel(f'{USER_HOST}:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel) # สร้าง Stub สำหรับเรียกใช้ Service
        request = user_pb2.UserRequest(user_id=user_id) # สร้าง Request ตามโครงสร้าง Proto
        try:
            response = stub.GetUser(request) # เรียกใช้ Method GetUser
            return {
                "user_name": response.user_name,
                "email": response.email,
                "is_active": response.is_active
            }
        except grpc.RpcError as e:
            return {"error": str(e.details())}

def get_order_info(user_id: int):
    """ฟังก์ชันดึงข้อมูลคำสั่งซื้อจาก Service C ผ่าน gRPC"""
    # เชื่อมต่อไปยัง Service C (Port 50052)
    with grpc.insecure_channel(f'{ORDER_HOST}:50052') as channel:
        stub = order_pb2_grpc.OrderServiceStub(channel)
        request = order_pb2.OrderRequest(user_id=user_id)
        try:
            response = stub.GetOrders(request)
            return {
                "items": list(response.items),
                "total_price": response.total_price
            }
        except grpc.RpcError as e:
            return {"error": str(e.details())}