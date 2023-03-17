# Write a program to calculate the age and tell them their age priority..

age = int(input(">> Enter Your Age : "))


if age > 0:

    if age > 0 and age <= 10:
        print("You Are A Child !")

    elif age >= 11 and age <= 18 :
        print("You Are A Teenager !")
    elif age >= 19 and age <= 28:
        print("You Are A young Person !")

    elif age >= 28 and age <= 35:
        print("You Are A Matured person !")
        

    else:
        if age >= 36 and age <= 55:
            print("You Are Tends To Old !")

        elif age >= 56 and age <= 70:
            print("You Are Old Person !")

        elif age >= 71 and age <= 100:
            print("You Are Too Old !")
        elif age > 100:
            print("You Are Legend Old !")

else:
    print("Please Enter A Number Greater Than 0 (zero) !")