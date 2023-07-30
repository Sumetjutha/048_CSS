import websocket
import json

# เชื่อมต่อกับ websocket ของราคาทอง
ws = websocket.WebSocketApp("wss://ws.finnhub.io/v1/stock/real-time?symbol=GC=F", on_message=on_message)
ws.on_error = on_error
ws.on_close = on_close
ws.run_forever()

# ฟังก์ชันสำหรับรับข้อความจาก websocket
def on_message(ws, message):
    # แปลงข้อความเป็น JSON
    data = json.loads(message)

    # รับราคาทอง
    price = data["price"]

    # คำนวณการเปลี่ยนแปลงของราคาทอง
    change = price - previous_price

    # แสดงราคาทองและการเปลี่ยนแปลงของราคาทอง
    print("ราคาทอง:", price)
    print("การเปลี่ยนแปลงของราคาทอง:", change)

    # บันทึกราคาทองล่าสุด
    previous_price = price

# ฟังก์ชันสำหรับจัดการข้อผิดพลาด
def on_error(ws, error):
    print(error)

# ฟังก์ชันสำหรับจัดการการปิดการเชื่อมต่อ
def on_close(ws):
    print("การเชื่อมต่อถูกปิด")

# เริ่มต้นการเชื่อมต่อ
ws.connect()