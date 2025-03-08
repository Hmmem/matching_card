Matching Card Game
ภาพรวมของโปรแกรม

Matching Card Game เป็นเกมจับคู่การ์ดที่พัฒนาด้วย Python และเฟรมเวิร์ก Kivy ผู้เล่นต้องจับคู่การ์ดที่มีสัญลักษณ์เดียวกันให้ครบทุกคู่โดยจะมีการจับเวลาที่ใช้ในการเล่น โดยมีฟีเจอร์ต่าง ๆ ดังนี้
เลือกระดับความยาก (Easy, Medium, Hard), ระบบจับเวลาและ Best Time, ปุ่มหยุดเวลาชั่วคราว, ปุ่มตั้งค่าหยุดเกมชั่วคราว, เพลงพื้นหลังและเอฟเฟกต์เสียง

การรันโปรแกรม

1.ทำการติดตั้ง dependencies: pip install kivy
2.รันโปรแกรม: python main.py

การทำงานของโค้ด

ใช้ ScreenManager ในการจัดการ 3 หน้าจอหลัก
1.เมนูหลัก (Mainmenuscreen)
2.เลือกความยาก (DifficultyScreen)
3.หน้าเกม (Gamescreen)

กระบวนการทำงาน
1.เริ่มจากโปรแกรม main.py
    1.1โหลดไฟล์สไตล์ Kivy (.kv) สำหรับ UI
    1.2สร้าง ScreenManager และเพิ่มหน้าจอ 3 หน้าจอ
    1.3ควบคุมเพลงพื้นหลัง 

2.หน้าจอเลือกความยาก difficulty_screen.py
    2.1แสดงปุ่มเลือกความยาก (Easy, Medium, Hard)
    2.2อัปเดต Best Time จากหน้าเกมผ่านเมธอด update_best_time()

3.หน้าเกม game_screen.py
    3.1ระบบจับเวลาจะทำการนับเวลาตั้งแต่เริ่ม-จนจบเกม แสดงผลในรูปแบบ MM:SS.MS
    3.2ระบบ Best Time: เปรียบเทียบเวลาปัจจุบันกับ Best Time และอัปเดต
    3.3การ์ดและกริด: สร้างการ์ดตามจำนวนคู่ที่กำหนดโดย CardManager
    3.4ฟีเจอร์
        3.4.1Time Stop: หยุดเวลา 5 วินาที (ใช้ได้ครั้งเดียวต่อเกม)
        3.4.2Pause Menu: หยุดเกมชั่วคราวและแสดง Popup

4.ตรรกะเกม logic_game.py
    4.1สร้างการ์ดโดยจะทำการสุ่มตัวอักษรภาษาอังกฤษและเพิ่มลงในกริด
    4.2ตรวจสอบการจับคู่
        4.2.1เมื่อเลือกการ์ด 2 ใบ จะทำการตรวจสอบ
        4.2.2หากตรงกันจะซ่อนการ์ดด้วย Animation
        4.2.3ถ้าไม่ตรงกันจะทำการพลิกการ์ดกลับ
    4.3การจบเกม เมื่อจับคู่ครบทุกคู่ จะหยุดเวลาและบันทึก Best Time

5.การ์ดและ Animation cards.py
    5.1คลาส Card สืบทอดจาก Button
    5.2การพลิกการ์ด ใช้ Animation เพื่อลดความกว้างเป็น 0 แล้วคืนค่า