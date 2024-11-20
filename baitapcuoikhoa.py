def write_ativity(content) :
    with open("ativity.txt","a") as f:
        f.write(content + "/n")

def write_error(content) :
    with open("error.txt","a") as f :
        f.write(content + "/n")

def create_user(name,age,email):
    global now
    write_ativity(f"[{now}] Bắt đầu tạo user ")
    try:
        name = input("nhập tên user")
        age  =  int(input("nhập tuổi user"))
        email = input("nhập email user")
        with open("list_user.txt","a") as f:
            f.write(f"Tên: {name} - Tuổi: {age} - Email: {email}\n")
    except:
        write_error(f"[{now}] Lỗi khi tạo user ")
    write_ativity(f"[{now}] Tạo user thành công ")
    print("Cập nhật user thành công")
    print(f"Tên: {name} - Tuổi: {age} - Email: {email}\n")

def update_user (user_info,new_value) :
    found = 0
    with open("list_user.txt","r") as f:
        list_user = f.readline()

    for user in list_user :
        if user_info in user :
            found += 1
            list_user[list_user.index(user)] = user.replace(user_info , new_value)

    with open("list_user.txt" , "w") as f:
        for user in list_user :
            f.write(user +"\n")

def delete_user(user_info) :
    found = 0
    with open("list_user.txt","r") as f:
        list_user = f.readline()

    for user in list_user : 
        if user_info in user :
            found += 1 
            list_user.remove(user)
            
    with open("list_user.txt" , "a") as f:
        for user in list_user:
            f.write(user+ "\n")

    return found

def show_info_user(user_info) :
        with open("list_user.txt" , "r") as f:
            list_user = f.readline()

        for user in list_user:
            if user_info in list_user:
                print(user)

while True :
    print("Menu")
    print("1. Tạo user")
    print("2. Cập nhật user")
    print("3. Xóa user")
    print("4. Tìm kiếm user")
    print("5. Thoát")
    choice = int(input("Nhập lựa chọn"))
    if choice == 1 :
        create_user()
    elif choice == 2 :
        user_info = input("Nhập thông tin user cần tìm:")
        new_value = input("Nhập thông tin user mới:")
        found =  update_user(user_info, new_value)
        if found == 0 :
            print("Ko tìm thấy user")
        else :
            print("Xóa user thành công")
    elif choice == 3 :
        user_info = input("Nhập thông tin user cần tìm:")
        found = delete_user(user_info)
        if found == 0 :
            print("Ko tìm thấy user")
        else :
            print("Xóa user thành công")
    elif choice == 4 :
        user_info = input("Nhập thông tin user cần tìm:")
        show_info_user(user_info)
    elif choice == 5 :
        print("Chương trình kết thúc")
        break