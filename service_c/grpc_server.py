import grpc
from concurrent import futures
import order_pb2
import order_pb2_grpc

ORDER_DB = {
    1: {
        "items": ["Holy Water", "Ancient Grimoire", "Saint's Prayer Beads"], 
        "total_price": 5000.0
    },
    2: {
        "items": ["Tea Set", "Strategy Book on Revenge", "Gift for Philia"], 
        "total_price": 1500.0
    }
}

class OrderServiceServicer(order_pb2_grpc.OrderServiceServicer):
    def GetOrders(self, request, context):
        order = ORDER_DB.get(request.user_id)
        if order:
            return order_pb2.OrderReply(
                user_id=request.user_id,
                items=order["items"],
                total_price=order["total_price"]
            )
        else:
            return order_pb2.OrderReply(user_id=request.user_id, items=[], total_price=0.0)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)
    server.add_insecure_port('[::]:50052') # Port 50052 (อย่าให้ซ้ำกับ Service A)
    print("Service C (Order) gRPC running on port 50052...")
    server.start()
    server.wait_for_termination()