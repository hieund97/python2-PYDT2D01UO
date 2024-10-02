# dict = {'apple': 5, 'banana': 10, 'orange': 15}
# name = "Phát"

# list = [1,2,3,4]


# try:
#     # print(dict['coconut'])
#     x = 100
#     y = 0
#     z = x / y
#     print(z)
# except KeyError as e:
#     print(e)
# except NameError as e:
#     print("Biến không tồn tại")
# except ZeroDivisionError as e:
#     print("không thể chia cho 0")
# except:
#     print("Co loi xay ra")
    
    

list_menu_fruit = {
    'apple': 20000,
    'banana': 30000,
    'orange': 40000,
    'mango': 50000,
    'strawberry': 60000,
    'watermelon': 70000,
    'pineapple': 80000,
    'grape': 90000,
    'cherry': 100000,
}



def display_menu(list_menu_fruit):
    print("---MENU---")
    for key,value in list_menu_fruit.items():
        print(f"{key} - giá: {value}/1kg")
        
while True:
    print("____CỬA HÀNG FRUIT XIN CHÀO____")
    print("____NHẬP LỰA CHỌN____")
    print("1. Hiên thị menu")
    print("2. Mua hàng")
    print("3. Kiểm tra hoá đơn")
    print("4. Thoát")
    choice = int(input("Nhập lựa chọn: "))
    if choice == 1:
        display_menu(list_menu_fruit)
    elif choice == 4:
        print("Chào tạm biệt")
        break
        
    


"""
1. Hiển thị menu
-> hiện thị được menu theo dictionary trên theo mẫu như sau:

1. apple - giá: 20000/1kg
2. banana - giá: 30000/1kg
3. orange - giá: 40000/1kg
4. mango - giá: 50000/1kg
5. strawberry - giá: 60000/1kg
6. watermelon - giá: 70000/1kg
7. pineapple - giá: 80000/1kg
8. grape - giá: 90000/1kg
9. cherry - giá: 100000/1kg


2. Mua hàng
+ input: nhập loại trái cây
+ input: nhập số lượng (kg)

-> hoá đơn:

3. Kiểm tra hoá đơn
 in hoá đơn 

1. apple - 3kg - Tổng: 60000 đồng
2. banana - 5kg - Tổng: 150000 đồng

Tổng tiền: 210000 đồng

Chú ý: kiểm tra nếu không tồn tại trái cây thì báo cho người dùng trái cây ko tồn tại
Kiểm tra khi người dùng nhập số lượng kg phải là 1 số, nhập sai phải báo lỗi


"""


    