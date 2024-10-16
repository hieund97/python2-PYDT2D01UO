# Tuần tự

list = [1,2,3,4,5,6,7,8,9,10,"hello", "Xin chèo", "Ni hao", "Bojou", "Hola"]

search_value = input("Nhap vao gia tri can tim kiem: ")

# chỉ phù hợp đối với danh sách ít phần tử -> chậm
for i in range(len(list)):
    if search_value == list[i]:
        print(f"{search_value} nằm ở vị trí thứ {i} trong danh sách")
        

# Nhị phân

a = int(input("nhap vao mot so nguyen duong: "))
list2 = [10,5,6,7,8,11,12,15,16]

def tim_kiem_nhi_phan(a, list2):
    low = 0
    high = len(list2) - 1

    while low <= high:
        mid = (low + high) // 2
        if a == list2[mid]:
            return mid
        elif a < list2[mid]:
            high = mid - 1
        elif a > list2[mid]:
            low = mid + 1 
    return None


vi_tri = tim_kiem_nhi_phan(a, list2)

if vi_tri is None:
    print(f"{a} khong nam trong danh sach")
else:
    print(f"{a} nam tai vi tri {vi_tri} trong danh sach")
        
        

"""
Đối với danh sách có ít phần tử
    + thuật toán tìm kiếm tuần tự -> Nhanh hơn

Đối với danh sách có nhiều phần tử
    + thuật toán tìm kiếm nhị phân -> Nhanh hơn
"""




