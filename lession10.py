
# giá trị sau khi sử dụng thư viện math có kiểu dữ liệu: 
# int -> làm tròn
# tính toán -> float

import datetime
import random


operation = ['+', '-', '*']
count = 0 # số câu trả lời đúng



so_lan_choi = int(input("Nhập số phép tính muốn chơi: "))

for i in range(so_lan_choi):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(operation)
    
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b

    now = datetime.datetime.now()
    user_answer = int(input(f"Nhâp câu trả lời cho phép tính: {a} {op} {b}: " ))
    now_2 = datetime.datetime.now()
    
    if user_answer == result:
        print("Câu trả lời chính xác")
        print("Thời gian trả lời là: ", now_2 - now)
        count += 1
    else:
        print("Câu trả lời không chính xác")
        print("Đáp án đúng là: ", result)
        print("Thời gian trả lời là: ", now_2 - now)
        
print("Trò chơi kết thúc")
print("Số câu trả lời đúng: ", count)
        
