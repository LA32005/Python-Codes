def main():
    print("[1]A,[2]B,[3]C,[4]D,[5]E,[6]F,[7]G,[8]H,[9]I,[10]J,[11]K,[12]L,[13]M,[14]N,[15]0,[16]P,[17]Q,[18]R,[19]S,[20]T,[21]U,[22]V,[23]W,[24]X,[25]Y,[26]Z")
    sc=input("Select letter:")

    
    if sc=="1":#A
        for row in range(7):
            for col in range(6):
                if (col==0 and row!=0) or (col==5 and row!=0)or((col>=1 and col<=4)and row==0)or((col>=1 and col<=4)and row==3):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    
    if sc=="2":#B
        for row in range(7):
            for col in range(6):
                if (col==0 or (row==0 and col!=5))or (row==6 and col!=5)or(col==5 and row!=3 and row!=0 and row!=6)or(row==3 and col!=5):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="3":#C
        for row in range(7):
            for col in range(6):
                if (col==0 and (row!=6 and row!=0))or (col>=1 and row==0)or (col>=1 and row==6)or(col==2 and row==1 and row==5):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="4":#D
        for row in range(7):
            for col in range(7):
                if (col==0 or (row==0 and col<=2))or (row==6 and col<=2)or (col==4 and row==1)or(col==4 and row==5)or (col==5 and row==2 )or (col==5 and row==4) or (col==5 and row==3):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="5":#E
        for row in range(7):
            for col in range(6):
                if (col==0 or row==0)or (row==3 or row==6):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="6":#F
        for row in range(7):
            for col in range(6):
                if ((col==0 or row==0)or row==3):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="7":#G
        for row in range(7):
            for col in range(8):
                if (col==0 and row!=6)or( col!=0  and col!=7 and row==6)or((col==7 and row>=4) and row<=5)or(row==0 and col<=5)or(row==4 and col>=3)or(col==6 and row==1):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    
    if sc=="8":#H
        for row in range(7):
            for col in range(6):
                if ((col==0 or col==5) or row==3):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="9":#I
        for row in range(6):
            for col in range(7):
                if ((row==0 or row==5)or col==3):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="10":#J
        for row in range(7):
            for col in range(9):
                if (col==4 or row==0)or ((col<=4 and row==6) and col!=0)or (col==0 and row==5) :
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="11":#K
        for row in range(7):
            for col in range(6):
                if (col==0) or(col==2 and row==3)or(col==3 and row==2)or(col==3 and row==4)or (col==4 and row==1)or(col==4 and row==5)or (col==5 and row==0)or(col==5 and row==6):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="12":#L
        for row in range(7):
            for col in range(6):
                if (row==6 or col==0):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="13":#M
        for row in range(7):
            for col in range(10):
                if (col==9 or col==0)or(row==1 and col==2)or(col==7 and row==1)or(row==2 and col==6)or(row==2 and col==3)or (row==3 and col==5):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="14":#N
        for row in range(7):
            for col in range(7):
                if (col==0 or col==6)or(col==1 and row==1)or(col==2 and row==2)or(col==3 and row==3)or(col==4 and row==4)or(col==5 and row==5)or(col==8 and row==6):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="15":#O
        for row in range(7):
            for col in range(10):
                  if (col==0 and row!=0 and row!=6)or (col==7 and row!=0 and row!=6)or (row==0 and col!=0 and col<=6)or(row==6 and col!=0 and col<=6):
                    print("*",end="")
                  else:
                    print(end=" ")
            print()

      
    if sc=="16":#P
        for row in range(7):
            for col in range(6):
                if (col==0 or (row==0 and col<=4)or row==3 and col<=4)or (row==1 and col==5)or (row==2 and col==5):
                    print("*",end="")
                else:
                    print(end=" ")
            print()
    

      
    if sc=="17":#Q
        for row in range(7):
            for col in range(10):
                if (col==0 and row!=0 and row!=6)or (col==7 and row!=0 and row!=6)or (row==0 and col!=0 and col<=6)or(row==6 and col!=0 and col<=6)or (row==6 and col==9)or(row==4 and col==5) :
                    print("*",end="")
                else:
                    print(end=" ")
            print()

      
    if sc=="18":#R
        for row in range(7):
            for col in range(7):
                if (col==0 or (row==0 and col<=4)or row==3 and col<=4)or (row==1 and col==5)or (row==2 and col==5)or(col==3 and row==4)or(col==4 and row==5)or (row==6 and col==5):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

      
    if sc=="19":#S
        for row in range(10):
            for col in range(8):
                if(col==0 and row!=0 and row<=3)or (row==0 and col!=0 and col!=7)or (row==4 and col!=0 and col!=7)or(row>=5 and row<=7 and col==7)or(row==8 and col!=7 and col!=0)or(row==1 and col==7)or(row==7 and col==0):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="20":#T
        for row in range(6):
            for col in range(7):
                if (col==3 or row==0):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="21":#U
        for row in range(6):
            for col in range(8):
                if ((col==0 or col==7) and row!=5)or (row==5 and col!=0 and col!=7):
                    print("*",end="")
                else:
                    print(end=" ")
            print()


    if sc=="22":#V
        for row in range(5):
            for col in range(9):
                if ((col==0 or col==8  )and row==0 )or ((col==1 or col==7  )and row==1 )or((col==2 or col==6)and row==2 )or((col==3 or col==5)and row==3 )or(col==4 and row==4 ):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    if sc=="23":#W
        for row in range(5):
            for col in range(17):
                if ((col==0 or col==8 or col==16 )and row==0 )or ((col==1 or col==7 or col==9 or col==15  )and row==1 )or((col==2 or col==6 or col==10 or col==14)and row==2 )or((col==3 or col==5 or col==11 or col==13)and row==3 )or((col==4 or col==12 )and row==4 ):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    
    if sc=="24":#X
        for row in range(7):
            for col in range(15):
                if (col==0  and (row==0 or row==6)) or(col==2 and (row==1 or row==5))or(col==4  and (row==2 or row==4))or(col==6 and row==3)or(col==8  and  (row==4 or row==2))or(col==10 and (row==5 or  row==1))or(col==12 and (row==6 or  row==0)) :
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    
    if sc=="25":#Y
        for row in range(6):
            for col in range(7):
                if (col==3 and row>=3)or((col==0 or col==6) and row==0) or ((col==1 or col==5) and row==1)or ((col==2 or col==4) and row==2):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    
    if sc=="26":#Z
        for row in range(6):
            for col in range(8):
                if (row==0 or row==5)or(row==1 and col==6)or (row==2 and col==5)or(row==3 and col==3)or(row==4 and col==1):
                    print("*",end="")
                else:
                    print(end=" ")
            print()
    main()
main()

    
