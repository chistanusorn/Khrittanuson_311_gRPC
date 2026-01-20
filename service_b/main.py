from fastapi import FastAPI # นำเข้าตัวจัดการ API
from fastapi.responses import HTMLResponse# นำเข้าคลาสสำหรับส่ง HTML กลับไปยังผู้ใช้
from grpc_client import get_user_info, get_order_info # นำเข้าฟังก์ชัน gRPC Client ที่เราเขียนไว้

app = FastAPI(title="Service B - Holy Dashboard Service")

# --- รูปภาพตัวอย่าง (Placeholder Image URLs) ---
# ท่านสามารถเปลี่ยน URL ตรงนี้เป็นลิ้งค์รูปภาพที่ท่านต้องการได้เลยค่ะ
PHILIA_IMAGE_URL = "https://i.pinimg.com/736x/17/7c/45/177c45d209714e1f2773229c86638194.jpg" 
MIA_IMAGE_URL = "https://i.pinimg.com/736x/a8/4a/1d/a84a1d70242750dcf5a17a64c0bf24b4.jpg"    

@app.get("/saints-profile") # สำหรับส่งงานแบบ JSON
def get_json():
    u1, o1 = get_user_info(1), get_order_info(1)
    u2, o2 = get_user_info(2), get_order_info(2)
    return {
        "owner": "Khitanuson 311",
        "results": [{"user": u1, "orders": o1, "image": PHILIA_IMAGE_URL}, {"user": u2, "orders": o2, "image": MIA_IMAGE_URL}]
    }

@app.get("/dashboard", response_class=HTMLResponse) # สำหรับหน้าเว็บ HTML สวยๆ พร้อมรูปภาพ!
def get_html():
    u1, o1 = get_user_info(1), get_order_info(1)
    u2, o2 = get_user_info(2), get_order_info(2)
    
    # --- CSS Styles สำหรับตกแต่งการ์ดและรูปภาพ ---
    card_style = """
        background: white; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
        margin-bottom: 20px; 
        display: flex; 
        align-items: center;
        border-left: 5px solid #6a1b9a;
    """
    image_style = """
        width: 80px; 
        height: 80px; 
        border-radius: 50%; 
        margin-right: 20px; 
        border: 3px solid #ce93d8;
        object-fit: cover;
    """
    
    return f"""
    <html>
        <head>
            <title>Dashboard</title>
        </head>
        <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f3e5f5; padding: 50px;">
            <h1 style="color: #4a148c; text-align: center;">✨ Dashboard ✨</h1>
            <p style="text-align: center; color: #7b1fa2;">Developer: <b>Khitanuson 311</b></p>
            <hr style="border-color: #e1bee7;">
            
            <div style="{card_style}">
                <img src="{PHILIA_IMAGE_URL}" alt="Philia" style="{image_style}">
                <div>
                    <h2 style="margin: 0; color: #6a1b9a;">{u1.get('user_name')}</h2>
                    <p style="color: #8e24aa;">📧 Email: {u1.get('email')}</p>
                    <p style="color: #4a148c; font-weight: bold;">🎒 Inventory: <span style="color: #d81b60;">{', '.join(o1.get('items', []))}</span></p>
                </div>
            </div>
            
            <br>
            
            <div style="{card_style} border-left-color: #c2185b;"> <img src="{MIA_IMAGE_URL}" alt="Mia" style="{image_style} border-color: #f48fb1;">
                <div>
                    <h2 style="margin: 0; color: #c2185b;">{u2.get('user_name')}</h2>
                    <p style="color: #8e24aa;">📧 Email: {u2.get('email')}</p>
                    <p style="color: #4a148c; font-weight: bold;">🎒 Inventory: <span style="color: #d81b60;">{', '.join(o2.get('items', []))}</span></p>
                </div>
            </div>
            
            <p style="text-align: center; margin-top: 40px; color: #aaa; font-size: 0.8em;">Powered by FastAPI, gRPC & Docker (and Pure Hatred for Tyrants! ❤︎)</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)