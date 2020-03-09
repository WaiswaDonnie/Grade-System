#Program to print out the grade

marks = int(input("ENter Student Marks\n"))


if marks>=100 or marks<0:
    print("Invalid mark, Marks should be between 0-100")
else:
    if marks >=80:
        print("D1")
    elif marks >=75:
        print("D2")
    elif marks >=65:
        print("C3")
    elif marks >=60:
        print("C4")
    elif marks >=55:
        print("c5")
    elif marks >=50:
        print("C6")
    elif marks >=45:
        print("P7")
    elif marks >=40:
        print("P8")
    else:
        print("F9")
    