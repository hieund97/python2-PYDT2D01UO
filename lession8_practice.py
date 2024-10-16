def tim_kiem_tuan_tu(value, list):
    for i in range(len(list)):
        if value == list[i]:
            return i
    return None


def tim_kiem_nhi_phan(value, list):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if value == list[mid]:
            return mid
        elif value < list[mid]:
            high = mid - 1
        elif value > list[mid]:
            low = mid + 1
    return None

def buble_sort(list):
    for i in range(len(list) - 1):
        for j in range(0, len(list) - i -1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

list_number = [87, 20, 51, 7, 85, 15, 9, 57, 51, 67, 13, 98, 9, 7, 15, 2, 25, 22, 74, 72]

search_value = int(input("nhap vao mot so nguyen cần tìm kiếm: "))

kq_tuan_tu = tim_kiem_tuan_tu(search_value, list_number)
kq_nhi_phan = tim_kiem_nhi_phan(search_value, buble_sort(list_number))

if kq_tuan_tu is None:
    print(f"{search_value} không tìm thấy")
else:
    print(f"{search_value} nam tai vi tri {kq_tuan_tu} trong danh sách bằng thuật toán tìm kiếm tuần tự")
    print(f"{search_value} nam tai vi tri {kq_nhi_phan} trong danh sách bằng thuật toán tìm kiếm nhị phân")