f = open('tracnghiem.txt', 'r')
list = f.readlines()

tot_bung = input(list[0])
if tot_bung == '1':
    ket_qua_cau_1 = "Đúng"
else:
    ket_qua_cau_1 = "Sai"

dang_yeu = input(list[1])
if dang_yeu == '2':
    ket_qua_cau_2 = "Đúng"
else:
    ket_qua_cau_2 = "Sai"

that_tha = input(list[2])
if that_tha == '3':
    ket_qua_cau_3 = "Đúng"
else:
    ket_qua_cau_3 = "Sai"

hay_hot = input(list[3])
if hay_hot == '4':
    ket_qua_cau_4 = "Đúng"
else:
    ket_qua_cau_4 = "Sai"
f.close()

f = open('trac_nghiem_ket_qua.txt', 'w')
f.write(f"Câu 1: {ket_qua_cau_1}\n")
f.write(f"Câu 2: {ket_qua_cau_2}\n")
f.write(f"Câu 3: {ket_qua_cau_3}\n")
f.write(f"Câu 4: {ket_qua_cau_4}\n")
f.close()

with open('trac_nghiem_ket_qua.txt', 'r') as f:
    ket_qua = f.read()

print(ket_qua)
