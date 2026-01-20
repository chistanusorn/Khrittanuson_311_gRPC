import grpc
from concurrent import futures
import order_pb2 # ไฟล์ที่สร้างจาก order.proto
import order_pb2_grpc

# ฐานข้อมูลคำสั่งซื้อไอเทมศักดิ์สิทธิ์
ORDER_DB = {
    1: {"items": ["Holy Water", "Ancient Grimoire"], "total_price": 5000.0},
    2: {"items": ["Premium Tea Set", "Strategy Book on Revenge"], "total_price": 1500.0},
}

class OrderServiceServicer(order_pb2_grpc.OrderServiceServicer):
    def GetOrders(self, request, context):
        """รับ user_id มาแล้วส่งรายการสินค้ากลับไป"""
        user_id = request.user_id
        order = ORDER_DB.get(user_id)
        
        if order:
            return order_pb2.OrderReply(
                user_id=user_id,
                items=order["items"],
                total_price=order["total_price"]
            )
        return order_pb2.OrderReply(user_id=user_id, items=[], total_price=0.0)

def serve():
    # รันเซิร์ฟเวอร์ gRPC สำหรับข้อมูล Order
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)
    # ใช้พอร์ต 50052 เพื่อไม่ให้ชนกับ User Service
    server.add_insecure_port('[::]:50052')
    print("Starting Order gRPC server on port 50052...")
    server.start()
    server.wait_for_termination()