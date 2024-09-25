import random

rank = []


def math():
    operator = ["+", "-", "*", "/"]

    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)

    random_operator = random.choice(operator)

    if random_operator == "+":
        string_math = f"{number_1} + {number_2} = "
        result = number_1 + number_2
    elif random_operator == "-":
        string_math = f"{number_1} - {number_2} = "
        result = number_1 - number_2
    elif random_operator == "*":
        string_math = f"{number_1} * {number_2} = "
        result = number_1 * number_2
    elif random_operator == "/":
        string_math = f"{number_1} / {number_2} = "
        result = round(number_1 / number_2, 2) 

    user_result = float(input(f"Nhap ket qua cua phep tinh: {string_math}"))

    if user_result == result:
        print("Câu trả lời chính xác")
        return 1
    else:
        print("Câu trả lời sai")
        print(f"Đáp án là: {result}")
        return 0


def display_rank():
    rank.sort(key=lambda x: x[1], reverse=True)
    if not rank:
        print("BXH chưa có người chơi")
    else:
        for i in range(len(rank)):
            print(f"{i+1}. {rank[i][0]} - {rank[i][1]}")


while True:
    print("1. Choi tro choi")
    print("2. Xem bang xep hang")
    print("3. thoat")

    choice = int(input("Chon chuc nang: "))

    if choice == 1:
        point = 0
        user_name = input("Hay nhap ten cua ban: ")
        for i in range(3):
            point += math()
            print("Chương trình kết thúc")
            print(f"Bạn đạt được {point}")

        rank.append([user_name, point])
    elif choice == 2:
        display_rank()
    elif choice == 3:
        print("Chương trình đã kết thúc")
        break
    else:
        print("Lựa chọn không hợp lệ")
