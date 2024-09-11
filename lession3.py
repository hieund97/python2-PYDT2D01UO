# list 2 chiều

# các phương thức sử dụng với list


# list =  [
#     [1,2,3,'a', 'b', 'c'],
#     ['python', 'java', 'C++', 'PHP'],
#     ['Python1', 'Boolen', 'String']
# ]

# Remove 
# list[1].remove('python')

# Pop -> Xoá 1 phần tử theo vị trí
# list[0].pop(0)

# Append -> chèn 1 giá trị vào cuối cùng của mảng
# list[0].append('Hello')



# len -> trả về số phần tử của list

# in -> Kiểm tra phần tử có nằm trong list hay không

# print(list)

# tuple = (1,2,3,10,4,5,6,7,8,9)

# list = ['a', 'b', 'c', 'd']

# tuple[0] = 'Xin chào'

# print(tuple)





regions = (
    ("Hà Nội", "10000"),
    ("Hồ Chí Minh", "70000"),
    ("Đà Nẵng", "55000"),
    ("Huế", "53000"),
    ("Quảng Ngãi", "80000"),
    ("Bình Định", 59000),
    ("Bình Thuận", 69000),
    ("Cà Mau", 79000),
    ("Kiên Giang", 89000),
    ("Đồng Nai", 99000),
    ("Tây Ninh", 52000),
    ("Lâm Đồng", 68000),
)

def display_location_info(location):
    for i in regions:
        if location in i:
            print(f"{i[0]} có mã vùng bưu điện là: {i[1]}")


def count_location():
    print(f"Trong cơ sở dữ liệu có {len(regions)} mã vùng bưu điện")


def check_location_exist(location):
    count = 0
    for i in regions:
        if location  in i:
            count += 1
    if count > 0:
        print(f"{location} có nằm trong cơ sở dữ liệu")
    elif count == 0:
        print(f"{location} không nằm trong cơ sở dữ liệu")

print("---MENU---")
print("1: Hiển thị thông tin địa phương")
print("2: Đếm số lượng ")
print("3: Kiểm tra địa phương có tồn tại hay không")
print("4: Thoát")

while True:
    choice = int(input("Nhập lựa chọn: "))
    if choice == 1:
        location = input("Nhập vùng cần hiện thi thông tin: ")
        display_location_info(location)
    elif choice == 2:
        count_location()
    elif choice == 3:
        location = input("Nhập vùng cần kiểm tra: ")
        check_location_exist(location)
    elif choice == 4:
        print("Chương trình kết thúc")
        break
    else:
        print("Lựa chọn không chính xác")