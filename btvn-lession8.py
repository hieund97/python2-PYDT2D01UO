def start():
    try:
        arr = []
        n = int(input("Nhập số lượng người chơi: "))

        for i in range(n):
            player_name = input("Nhập tên người chơi: ")
            play_score = int(input("Nhập diem của người chơi: "))
            arr.append((player_name, play_score))

        return arr

    except ValueError:
        print("Điểm số của người chơi phải là 1 số")
    except:
        print("Có lỗi xảy ra vui lòng thử lại")


def display_rank(arr):
    index = 1
    for i in arr:
        print(f"{index}: người chơi: {i[0]} - {i[1]} điểm")
        index += 1


def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(0, len(list) - i - 1):
            if list[j][1] < list[j + 1][1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list
    
    i = (target)
    input(target)


list_player = start()


print("Hiển thị BXH lúc đầu")
display_rank(list_player)


sort_list_player = bubble_sort(list_player)

print(list_player)

print(enumerate(list_player))


print("Hiển thị BXH đã được sắp xếp")
display_rank(sort_list_player)

target =  int(input("Nhập điểm số cần tìm: "))

found = False
#cach1
index = 1
for i in list_player:
    if i[1] == target:
        positon = index
        found = True
        break
    else:
        index += 1
        
#cach2  
# for i,(player_name, play_score) in enumerate(list_player, 1):
#     if play_score == target:
#         positon = i
#         found = True
#         break

if found:
    print(f"Điểm {target} ở Top {positon}")
else:
    print("Target score not found.")

        
    
# list_player = [
#    1 - ("player_1", 100),
#    2 - ("player_2", 200),
#    3 - ("player_3", 300),
# ]    

