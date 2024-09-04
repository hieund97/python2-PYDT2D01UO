# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# while True:
#     number = int(input("Nhập số: "))
#     if number in list1:
#         print(f"số {number} có nằm trong list1")
#         break
#     if number in list2:
#         print(f"số {number} có nằm trong list2")
#         break

# ["hồng", "hồng", "hồng" "hồng", "đỏ", "đỏ"]
# ["hồng", "hồng", "hồng" "đỏ", "đỏ", "đỏ"]
# ["hồng", "hồng", "hồng" "đỏ", "đỏ", "đỏ"]
# ["hồng", "hồng", "hồng" "hồng", "đỏ", "đỏ"]
# ["hồng", "hồng", "hồng" "hồng", "đỏ", "đỏ"]

# list 1 chiều
lst1 = ["hello", "Xin chào", 'Ni hao', 'Bojou', 'Hola']
# for i in lst1:
#     print(i)


#list 2 chiều

#Yêu cầu tính tổng của các số trong list. Gợi ý dùng vòng lặp for
# lst = [
#     [1,2,3,4,5,6,7,8], #0
#     [9,10,11,12,13,14,15,16,17], #1
#     [18,19,20,21,22,23,24,25], #2
# ]



#len là trả về số lượng phần tử của list
# print(len(lst[1]))

#append chèn vào vị trí cuối cùng của list
# lst[2].append("hello")

#pop xóa phần tử của list theo vị trí
# lst[0].pop(3)

#remove xóa phần tử của list theo giá trị của nó
# lst[0].remove("Xin chào")


# print(lst[0])


#Yêu cầu tính tổng của các số trong list. Gợi ý dùng vòng lặp for
lst = [
    [1,2,3,4,5,6,7,8], #0
    [9,10,11,12,13,14,15,16,17], #1
    [18,19,20,21,22,23,24,25], #2
]


# cách 1
# tong = 0
# for list_con in lst:
#     for j in i:
#         # tong = tong + j
#         tong += j
        
# print(tong)

# cách 2:

# sum là hàm tính tổng của 1 list (DdKien: List đó toàn bộ phải là int hoặc float)
# tong = 0
# for list_con in lst:
#     tong += sum(list_con)
    
# print(tong)


"""
Yêu cầu: Tạo ra 1 chương trình có 2 lựa chọn
Lựa chọn 1: Vẽ hình chữ nhật
Lựa chọn 2: Vẽ hình vuông

Hình chữ nhật
********
********
********

Hình vuông
* * * * *
* * * * *
* * * * *
* * * * *
"""

def draw_rectangle():
    for i in range(3):
        print("*" * 5)

def draw_square():
    for i in range(4):
        print("*" * 4)


while True:
    print("Chương trình vẽ hình")
    print("1. Hình chữ nhật")
    print("2. Hình vuông")
    choice = int(input("Nhập lựa chọn: "))

    if choice == 1:
        draw_rectangle()
    elif choice == 2:
        draw_square()
    else:
        print("Chương trình kết thúc")
        break
