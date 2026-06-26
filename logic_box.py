while True:
    print("welcome to the partten genrator and Analyzer")
    print("1)Right Angle traingle")
    print("2)Pyramid")
    print("3)Left Angle traingle")
    print("4)Analyze a range of number")
    print("5)Exit")
    
    choice=int(input("Enter your choice:"))
    if choice == 1.:
        print("enter your 1")
        rows=int(input("Enter the number of row:"))

        if rows<=0:
            print("Invaild rows...!")
            
        print("Right Angle traingle..")    
        for i in range(1,rows+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()

    elif choice==2:
        rows=int(input("Enter the number of row:"))
        if rows<=0:
            print("Invaild rows...!")
        print("pyramid pattern..!")
        for i in range(rows):
            for space in range (rows-i+1):
                print( " ",end=" ")
            for j in range(2*i+1):
                print("*",end=" ")
            print()

    elif choice==3:
        rows=int(input("Enter the number of row:"))
        if rows<=0:
            print("Invaild rows...!")
            
        print("Left Angle traingle..!")
        for i in range(1,rows+1):
            for space in range (rows-i+1):
                print( " ",end=" ")
            for j in range(i):
                print("*",end=" ")
            print()


    elif choice==4:
        start=int(input("Enter the starting number:"))
        end=int(input("Enter the ending number:"))
        if end<start:
            print("End number must be greater than start number...!")
            continue
        total = 0
        for i in range (start,end+1):
            if i==0:
                pass
            elif i%2 == 0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is odd")
            total += i
            
        print(f"Sum of all number from {start} to {end} is : {total}")
        