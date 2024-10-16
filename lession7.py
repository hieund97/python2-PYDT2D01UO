"""

int -> 1
float -> 1.5
string -> "hello"



list -> [1,2,3]
tuple -> (1,2,3,4)


Boolen -> True/False
Dict -> {'apple': 5, 'banana': 10, 'orange': 15}
set -> {1,2,3,4} -> Không có dữ liệu trùng nhau



"""


# list = [5,6,9,1,3,4,8,10,11]

# for i in range(len(list) - 1):
#     for j in range(0, len(list) - i -1):
#         if list[j] < list[j+1]:
#             tmp = list[j]
#             list[j] = list[j+1]
#             list[j+1] = tmp


# list = [885, 375, 841, 452, 780, 750, 244, 335, 274, 158, 105, 897, 204, 298, 118, 777, 450, 119, 425, 582, 728, 160, 308, 313, 357, 974, 625, 243, 829, 513, 888, 867, 715, 767, 510, 875, 388, 549, 114, 783, 759, 822, 359, 548, 149, 970, 268, 866, 525, 68, 936, 521, 528, 781, 506, 192, 19, 420, 129, 399, 888, 253, 60, 789, 549, 453, 203, 487, 841, 488, 645, 464, 346, 327, 225, 293, 207, 7, 628, 303, 757, 147, 736, 343, 645, 607, 336, 21, 318, 269, 940, 770, 986, 552, 420, 79, 820, 47, 380, 432]

# for i in range(len(list) - 1):
#     for j in range(0, len(list) - i -1):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
        
# print(list)


# order_status = {
#     "order1": "Đang xử lý",
#     "order2": "Đang xuất bán",
#     "order3": "Đã giao hàng",
#     "order4": "Đã huỷ",
#     "order5": "Giao hàng thành công",
#     "order6": "Chờ thanh toán",    
# }

# def check_order_status():
#     while True:
#         try:
#             order_id = input("Nhập mã đơn hàng: ")
#             # Kiểm tra đơn hàng có tồn tại hay không:
#             if order_id in order_status:
#                 print(f"Đơn hàng: {order_id} đang trong trạng thái: {order_status[order_id]}")
#                 break
#             else:
#                 print("Mã đơn hàng không tồn tại. Vui lòng thử lại.")
#                 continue
            
#         except:
#             print("Có lỗi xảy ra, vui lòng thử lại")
            
# check_order_status()

"""
1. Khang
2. Phúc
3. Phát

"""


try:
    a = [1,2,3,4,5]
    print(a[5])
except ValueError:
    print("Có lỗi xảy ra, vui lòng thử lại")
except IndexError:
    print("Có lỗi xảy ra lỗi index error")
        
        
