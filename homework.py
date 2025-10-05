# ข้อ 3: แสดงกราฟ line plot ของผลลัพธ์ทุกข้อในกราฟเดียวกัน

import matplotlib.pyplot as plt

# สมมติจากข้อ 2 มีสมการที่คำนวณผลลัพธ์ไว้ เช่น
# a = n + 2
# b = n * 2
# c = n ** 2

n_values = list(range(1, 11))  # กำหนดค่า n ตั้งแต่ 1-10
a_values = [n + 2 for n in n_values]
b_values = [n * 2 for n in n_values]
c_values = [n ** 2 for n in n_values]

# วาดกราฟ
plt.plot(n_values, a_values, label="n+2")
plt.plot(n_values, b_values, label="n*2")
plt.plot(n_values, c_values, label="n^2")

plt.xlabel("n")
plt.ylabel("ผลลัพธ์")
plt.title("Line plot ของผลลัพธ์จากสมการ")
plt.legend()
plt.grid(True)
plt.show()
