list_number = (
    ("Nguyen thi haha", "0918"),
    ("Tran thi huhu", "0856"),
    ("Trang nguyen phuc", "0902"),
    ("Nguyen thu hehe", "0925"),
)


def display_info():
    for contact in list_number:
        print(f"Người dùng tên: {contact[0]} - Số địen thoại: {contact[1]}")


def count_list_number():
    print(f"Trong cơ sở dữ liệu có {len(list_number)} số điện thoại")


def check_number(number):
    for contact in list_number:
        if number in contact:
            return contact

    print("Số địen thoại không tìm thấy trong dữ liệu")


while True:
    print("---MENU---")
    print("1. Hien thi thong tin")
    print("2. Dem so luong so dien thoai")
    print("3. Kiem tra so dien thoai co ton tai trong dữ liệu hay khong")
    print("4. Thoat")

    choice = int(input("Nhập lựa chọn: "))

    if choice == 1:
        display_info()
    elif choice == 2:
        count_list_number()
    elif choice == 3:
        number = input("Nhập số địen thoại cần kiểm tra: ")
        check = check_number(number)
        if check:
            print(f"Người dùng tên: {check[0]} - Số địen thoại: {check[1]}")
    else:
        print("Chương trình kết thúc")
        break
