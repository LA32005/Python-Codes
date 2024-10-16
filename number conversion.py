def main():
    print("[1] decimal to binary\n[2] decimal to octal\n[3] decimal to hexadecimal\n[4] binary to decimal\n[5] binary to octal\n[6] binary to hexadecimal\n[7] octal to binary\n[8] hexadecimal to binary\n[9] octal to hexadecimal\n[10] octal to decimal\n[11] hexadecimal to decimal\n[12] hexadecimal to octal")
    sc=input("select conversion: ")

    if sc=='1':#decimal to binary
        d=int(input("Enter Decimal number:"))
        if d > 0:
            BIN=""

            while d > 0:# it will continually divide the d until it becomes  to 0
                r=d%2 # to get the remainder of given/decimal first
                d=d//2 # to get the quotient of d then the answer will repeat the process until it becomes to 0
                BIN=str(r) + BIN # to add every remainder of each equation as a string  ex:  r=1 and BIN=0 ,r + BIN='10', then the answer will store to BIN until the d becomes 0,now r=1 and BIN='10' ,r + BIN='110' and so on
            print("BINARY:",BIN)

    elif sc=='2':# decimal to octal
        d=int(input("Enter Decimal:"))
        if d>0:
            OCT=""

            while d >0:
                r=d%8
                d=d//8
                OCT=str(r) + OCT
            print("OCTAL:",OCT)
    elif sc=='3':#decimal to hexadecimal
        d=int(input("Enter Decimal:"))
        if d>0:
            HEX=""

            while d>0:
                r=d%16                
                if r==1:
                    remainder="1"
                elif r==2:
                    remainder="2"
                elif r==3:
                    remainder="3"
                elif r==4:
                    remainder="4"
                elif r==5:
                    remainder="5"
                elif r==6:
                    remainder="6"
                elif r==7:
                    remainder="7"
                elif r==8:
                    remainder="8"
                elif r==9:
                    remainder="9"
                elif r==10:
                    remainder="A"
                elif r==11:
                    remainder="B"
                elif r==12:
                    remainder="C"
                elif r==13:
                    remainder="D"
                elif r==14:
                    remainder="E"
                elif r==15:
                    remainder="F"                              
                d=d//16
                HEX=remainder + HEX
            print("HEXADECIMAL:",HEX)

    elif sc=='4':#binary to decimal
        b=input("Enter Binary:")
        LEN=len(b)#length of binary
        SUM=0
        E=LEN-1 # exponent
        for x in range (LEN):
            if(b[x] =='0')or (b[x] =='1'):
                a=int(b[x])*2**(E)
                E=E-1
                SUM=SUM + a
        print("DECIMAL:",SUM)

    elif sc=='5':#binary to octal
        b=input("Enter Binary:")
        len1=len(b)
        sum1=0
        aa=len1-1
        for x in range(len1):
            if (b[x] == '0') or ( b[x] == '1'):
              a=int(b[x])* 2**(aa)

              aa=aa-1

              sum1=sum1 + a

        Dec=sum1
        if Dec >0:
            OCT= ""
           
            while Dec > 0:
                  r = Dec % 8
                  Dec=Dec// 8
                  OCT= str(r) + OCT
            print('OCTAL:',OCT)
      

    elif sc=='6':#binary to hexadecimal
         b= input("Enter Binary: ")
         len1=len(b)
         sum1=0
         aa=len1-1
         for x in range(len1):
            if (b[x] == '0') or ( b[x] == '1'):
                a=int(b[x])* 2**(aa)

                aa=aa-1

                sum1=sum1 + a
         Dec=sum1
         if Dec > 0:
            HEXA= ""
            r=("[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]")

            while Dec > 0:
                r = Dec%16
                if r==1:
                    remainder="1"
                elif r==2:
                    remainder="2"
                elif r==3:
                    remainder="3"
                elif r==4:
                    remainder="4"
                elif r==5:
                    remainder="5"
                elif r==6:
                    remainder="6"
                elif r==7:
                    remainder="7"
                elif r==8:
                    remainder="8"
                elif r==9:
                    remainder="9"
                elif r==10:
                    remainder="A"
                elif r==11:
                    remainder="B"
                elif r==12:
                    remainder="C"
                elif r==13:
                    remainder="D"
                elif r==14:
                    remainder="E"
                elif r==15:
                    remainder="F"
            
                Dec =Dec// 16    
                HEXA = remainder + HEXA
            print('HEXADECIMAL:',HEXA)

    elif sc=='7':
            o= input("Enter octal: ")
            len1=len(o)
            bi=""
            for x in range(len1):
                OCT = o[x]
                value ={"0": "000", "1": "001", "2": "010", "3": "011","4": "100", "5": "101", "6": "110", "7": "111"}#convert the number to its intended binary
                bi=bi + value[OCT]
            print("BINARY:",bi)

    elif sc=='8':#hexadecimal to  binary
         h= input("Enter Hexadecimal: ")
         len1=len(h)
         bi=""
         for x in range(len1):
             Hex = h[x]
             value ={"0": "0000", "1": "0001", "2": "0010", "3": "0011","4": "0100", "5": "0101", "6": "0110", "7": "0111","8": "1000", "9": "1001", "A": "1010", "B": "1011","C": "1100", "D": "1101", "E": "1110", "F": "1111"}
             bi=bi + value[Hex]
         print("BINARY:",bi)

    elif sc=='9':#octal to hexadecimal
        b=str(input("enter octal"))
        len1=len(b)
        sum1=0
        aa=len1-1
        for x in range(len1):
            a=int(b[x])* 8**(aa)

            aa=aa-1

            sum1=sum1 + a

        Dec=sum1
        if Dec >0:
           HEXA= ""
           
           while Dec > 0:
               r = Dec % 16
               if r==1:
                   remainder="1"
               elif r==2:
                   remainder="2"
               elif r==3:
                   remainder="3"
               elif r==4:
                   remainder="4"
               elif r==5:
                   remainder="5"
               elif r==6:
                   remainder="6"
               elif r==7:
                   remainder="7"
               elif r==8:
                   remainder="8"
               elif r==9:
                   remainder="9"
               elif r==10:
                   remainder="A"
               elif r==11:
                   remainder="B"
               elif r==12:
                   remainder="C"
               elif r==13:
                   remainder="D"
               elif r==14:
                   remainder="E"
               elif r==15:
                   remainder="F"
               Dec=Dec// 16
               HEXA= remainder + HEXA
           print('hexadecimal number:',HEXA)

    elif sc=='10':#octal to decimal
        b=str(input("enter octal"))
        len1=len(b)
        sum1=0
        aa=len1-1
        for x in range(len1):
            a=int(b[x])* 8**(aa)

            aa=aa-1

            sum1=sum1 + a
        print("DECIMAL:",sum1)

    elif sc=='11':#hexadecimal to decimal
        b=str(input("enter hexadecimal"))
        len1=len(b)
        sum1=0
        aa=len1-1
        for x in range(len1):
            b[x]=("[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]")
            if b[x]==1:
                b[x]="1"
            elif b[x]==2:
                b[x]="2"
            elif b[x]==3:
                b[x]="3"
            elif b[x]==4:
                b[x]="4"
            elif b[x]==5:
                b[x]="5"
            elif b[x]==6:
                b[x]="6"
            elif b[x]==7:
                b[x]="7"
            elif b[x]==8:
                b[x]="8"
            elif b[x]==9:
               b[x]="9"
            elif b[x]==10:
               b[x]="A"
            elif b[x]==11:
               b[x]="B"
            elif b[x]==12:
                b[x]="C"
            elif b[x]==13:
                b[x]="D"
            elif b[x]==14:
                b[x]="E"
            elif b[x]==15:
                b[x]="F"
            
            a=int(b[x])* 16**(aa)

            aa=aa-1

            sum1=sum1 + a
        print("DECIMAL:",sum1)

    if sc=='12':#hexadecimal to octal
        b=str(input("enter hexadecimal"))
        len1=len(b)
        sum1=0
        aa=len1-1
        for x in range(len1):
             a=int(b[x])* 16**(aa)

             aa=aa-1

             sum1=sum1 + a
        
        Dec=sum1
        if Dec >0:
            OCT= ""
           
            while Dec > 0:
                  r = Dec % 8
                  Dec=Dec// 8
                  OCT= str(r) + OCT
            print('OCTAL:',OCT)
    main()
main() 
                
        
