def Create( a, len ) :
    space =(a - len) * 5 
    for i in range (3) :
        print(" "* space, end = "")
        print("  " * (3 - i),end = "")
        for j in range(len) :
            print("* "*(i * 2 + 1),end = "")
            print("  " *((2 - i) * 2), end = "")
        print()
    if (len != a) :
        Create(a,len + 1)

a = int(input("nhập số: "))
Create(a ,1)


