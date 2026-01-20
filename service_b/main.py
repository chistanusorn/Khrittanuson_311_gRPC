# นำเข้าเครื่องมือสำหรับสร้าง API และจัดการ Error
from fastapi import FastAPI, HTTPException
# นำเข้าฟังก์ชันจากก grpc_client เพื่อไปคุยกับ Service อื่น
from grpc_client import get_user_info, get_order_info

# ประกาศสร้างตัวแปรแอป FastAPI
app = FastAPI(
    title="[คริสตนุสรณ์ มหาวีระตระกูล] [311] [FastAPI + gRPC Microservices Project]",
    description="โปรเจค Microservices (REST + gRPC) โดยนักศึกษาผู้มีวิสัยทัศน์",
    version="1.0.0"
)
# Endpoint สำหรับดึงข้อมูลรวมของ "นักบุญ" (Direct Mapping)
@app.get("/saints-profile")
def get_saints_profile():
    """
    ฟังก์ชันนี้ทำหน้าที่เป็นตัวกลาง (Aggregator) 
    โดยจะไปดึงข้อมูลจาก Service A และ Service C มารวมกัน
    """
    try:
        # ดึงข้อมูลผู้ใช้จาก Service A (เปรียบเสมือนท่านพี่ฟีเลีย ID 1)
        user1 = get_user_info(1)
        order1 = get_order_info(1)
        
        # ดึงข้อมูลผู้ใช้จาก Service A (เปรียบเสมือนตัวดิฉันเอง ID 2)
        user2 = get_user_info(2)
        order2 = get_order_info(2)

        # ส่งข้อมูลกลับไปหาผู้ใช้ในรูปแบบ JSON ตามที่ออกแบบไว้
        return {
            "project_owner": "Khitanuson 311", 
            "title": "The Holy Saints Student",
            "data": [
                {"name": user1.get("user_name"), "items": order1.get("items")},
                {"name": user2.get("user_name"), "items": order2.get("items")}
            ]
        }
    except Exception as e:
        # หากเกิดข้อผิดพลาด จะส่ง HTTP 500 กลับไป
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    # ต้องเป็น 0.0.0.0 ห้ามเป็น 127.0.0.1 หรือ localhost เด็ดขาด!
    uvicorn.run(app, host="0.0.0.0", port=8001)