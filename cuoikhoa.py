"""
Xây dựng chương trình quản lý người dùng và ghi lại nhật ký hoạt động
Mục tiêu:
Viết một chương trình Python có chức năng quản lý thông tin người dùng bao gồm:

Thêm người dùng mới.
Cập nhật thông tin người dùng.
Xóa người dùng.
Tìm kiếm người dùng.
Ngoài ra, chương trình sẽ ghi lại tất cả các thao tác (hoạt động) vào một file nhật ký activity.txt,
Nếu có lỗi thì ghi vào file error.txt

Nhập tên, tuổi và email của người dùng.
Ghi lại thông tin vào file users.txt.
Ghi nhật ký hoạt động vào file activity.txt.

Gợi ý

+ Tạo ra 1 hàm ghi vào file activity.text
+ tạo ra 1 hàm ghi vào file error.text

+ tao 4 hàm tương ứng CRUD với 1 user
    + Create -> lưu vào file list_user.txt
    + Read -> doc tu file list_user.txt
    + Update -> cap nhật user trong list_user.txt
    + Delete -> xóa user trong list_user.txt
Ghi vào file nhật ký activity.txt
nếu có lỗi sử dụng try except để ghi lỗi vào error.txt

Mẫu file list_user.txt:
Tên: Tuấn Phát - Tuổi: 15 - Email: phatgpt@gmail.com
Tên: Đức Khang - Tuôi: 15 - Email: khang@gmail.com
Tên: Trường - Tuổi: 15 - Email: truong@gmail.com
#thêm user

Mẫu file activity.txt:
[2024-11-06 12:00:00] - bắt đầu tạo mới user
[2024-11-06 12:05:00] - Tạo mới user thành công

Mẫu file error.txt
[2024-11-06 12:00:00] - Lỗi khi cập nhật user
[2024-11-06 12:05:00] - Lỗi khi xoá user


"""

import datetime as d

now = d.datetime.now()

def write_activity(content):
    with open("activity.txt", "a") as f:
        f.write(content + "\n")
        
def write_error(content):
    with open("error.txt", "a") as f:
        f.write(content + "\n")
        
        
#tạo ra 4 hàm
def create_user():
    global now
    write_activity(f"[{now}] Bắt đầu tạo user")
    try:
        name = input("Nhập tên user: ")
        age = int(input("Nhập tuổi user: "))
        email = input("Nhập email user: ")
        
        with open("list_user.txt", "a") as f:
            f.write(f"Tên: {name} - Tuổi: {age} - Email:{email}\n")
    except:
        write_error(f"[{now}] Lỗi khi tạo user")
    write_activity(f"[{now}] Tạo user thành công")
    print("Cập nhật user thành công")
    print(f"Tên: {name} - Tuổi: {age} - Email:{email})")

def update_user(user_info, new_value):
    found = 0
    with open("list_user.txt", "r") as f:
        list_user = f.readlines()
        
        
    # list_user.index(user) lấy ra index của user hiện tại
    for user in list_user:
        if user_info in user:
            found += 1
            list_user[list_user.index(user)] = user.replace(user_info, new_value)
    
    with open("list_user.txt", "w") as f:
        for user in list_user:
            f.write(user + "\n")
    
    return found
            

def delete_user(user_info):
    found = 0
    with open("list_user.txt", "r") as f:
        list_user = f.readlines()
        
    for user in list_user:
        if user_info in user:
            found += 1
            list_user.remove(user)
    
    with open("list_user.txt", "w") as f:
        for user in list_user:
            f.write(user + "\n")
            
    return found

def show_info_user(user_info):
    with open("list_user.txt", "r") as f:
        list_user = f.readlines()
        
    for user in list_user:
        if user_info in user:
            print(user)
            

while True:
    print("____MENU____")
    print("1. Tạo user")
    print("2. Cập nhật user")
    print("3. Xóa user")
    print("4. Tìm kiếm user")
    print("5. Thoát")
    choice = int(input("Nhập lựa chọn: "))
    if choice == 1:
        create_user()
    elif choice == 2:
        user_info = input("Nhập thông tin user cần tìm: ")
        new_value = input("Nhập thông tin user mới: ")
        found = update_user(user_info, new_value)
        if found == 0:
            print("Không tìm thấy user")
        else:
            print("Xoá user thàng công")
    elif choice == 3:
        user_info = input("Nhập thông tin user cần tìm: ")
        found = delete_user(user_info)
        if found == 0:
            print("Không tìm thấy user")
        else:
            print("Xoá user thàng công")
    elif choice == 4:
        user_info = input("Nhập thông tin user cần tìm: ")
        show_info_user(user_info)
    elif choice == 5:
        print("Chương trình kết thúc")
        break