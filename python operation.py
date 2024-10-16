def main():

    print('[1] Mathematical operation\n[2] Bitwise operation\n[3] Relational operation\n[4] Logical operation\n[5] Assignment operation\n[6] membership operation\n[7]Identity opeartion\n[8] complement')

    EC=input('Enter your choice: ')

    if EC=='1':
        num1=int(input('Enter first number: '))
        num2=int(input('Enter second number: '))
        op=input('Enter Mathematical operation [+,-,*,/,//,%,**]:')

        if op=='+':
            print(num1+num2)

        elif op=='-':
            print(num1-num2)
        elif op=='*':
            print(num1*num2)
        elif op=='/':
            print(num1/num2)
        elif op=='**':
            print(num1**num2)
        elif op=='%':
            print(num1%num2)
        elif op=="//":
            print(num1//num2)
        else:
            print('invalid input')
        main()
        

    if EC=='2':
         num1=int(input('Enter first number: '))
         num2=int(input('Enter second number: '))
         op=input('Enter Bitwise operation [~,^,|,&]: ')

         if op=='&':
             print(num1&num2)
         elif op=='|':
             print(num1 | num2)
         elif op=='~':
             print(~num1)
             print(~num2)
         elif op=='^':
             print(num1^num2)
         else:
             print('Invalid input')

    if EC=='3':
        op=input('Relational operation [==,!=,>,<,<=,>=]:')
        num1=int(input('Enter first number'))
        num2=int(input('Enter second number'))

        if op=='>':
            print(bool(num1>num2))
        elif op=='<':
            print(bool(num1<num2))
        elif op=='<=':
            print(bool(num1<=num2))
        elif op=='>=':
            print(bool(num1>=num2))
        elif op=='==':
            print(bool(num1==num2))
        elif op=='!=':
            print(bool(num1!=num2))
        else:
            print('invalid input')
        

    if EC=='4':
        op=input('Logical operation [>, <, >=, <=, ==, !=]:')
        num1=int(input('Enter first number'))
        num2=int(input('Enter second number'))

        if op=="or":
            if(A=='true' and B=='false'):
                print('True')
            elif(A=='false ' and B=='true'):
             print('True')
            elif(A=='true' and B=='true'):
             print('True')
            elif (A=='false' and B=='false'):
             print('False')
           
        elif op=="and":
           if(A=='true' and B=='false'):
             print('False')
           elif(A=='false' and B=='true'):
             print('False')
           elif(A=='false' and B=='false'):
             print('False')
           elif(A=='true' and B=='true'):
             print('True')
            
        elif op=="not":
            print(bool(A!=B))
        else:          
            print("invalid input")

     
        

    if EC=='5':
        num1=int(input('Enter first number: '))
        num2=int(input('Enter second number: '))
        op=input('Assignment operation [=, +=, -=, *=, /=, %=, **=, &=, |=, ^=]:')

        if op=='+=': 
           print(num1+num2)
        elif op=='-=':
           print(num1-num2)
        elif op=='*=':
            print(num1*num2)
        elif op=='/=':
            print(num1/num2)
        elif op=='%=':
            print(num1%num2)
        elif op=='**=':
            print(num1**num2)
        elif op=='&=':
            print(num1&num2)
        elif op=='|=':
            print(num1|num2)
        elif op=='^=':
            print(num1^num2)
        elif op=='=':
            print(num1,num2)
        else:
             print('Invalid input')


            
            

    elif EC=="6":#membership
         print("[1] List\n[2] Tuple\n[3] string")
         
         CT=input("Choose your type")
         if CT=="1":
             list=[]
             elem=int(input("Enter number of element:"))
             for x in range (elem):
                 a=int(input("Enter elements:"))
                 list.append(a)
             print("list:",list)
             A=int(input("Enter the element you want to check:"))

             if A in list:
                print(( A in list),A,"is in the list")
             else:
                print((A in list), A,"is not in the list")

         if CT=="2":
            list=[]
            tup=()
            element = int(input("Enter number of Element: "))
            for x in range(element):
                a = int(input("Enter Elements: "))
                list.append(a)
                tup=tuple(list)
            print(tup)
            A = int(input("Enter the element you want to check: "))
            if A in tup:
                print((A in tup), A,"is in the tuple")
            else:
                print((A in tup), A,"is not in the tuple")

         if CT=='3':
            word=input("Enter String: ")
            elem=input("Enter which element to check: ")
            
            if elem in word:
                print((elem in word),elem,'is in word')
            if elem not in word:
                print((elem in word),elem,'is not in word')

    elif EC=="7":# identity
        A=int(input("Enter the integer: "))
        B=float(input("Enter the float: "))
          
        print("What is the return value of type(A) is integer?\n ",type(A) is int)
        print("What is the return value of type(A) is float? \n ",type(A) is float)
        print("What is the return value of type(A) is str? \n",type(A) is str)
        print("What is the return value of type(A) is not integer?\n " ,type(A) is not int)
        print("What is the return value of type(A) is not float? \n",type(A) is not float)
        print("What is the return value of type(A) is not an str? \n",type(A) is not str)
        print("What is the return value of type(B) is integer? \n",type(B) is int)
        print("What is the return value of type(B) is float?  \n",type(B) is float)
        print("What is the return value of type(B) is str? \n",type(B) is str)
        print("What is the return value of type(B) is not integer?\n " ,type(B) is not int)
        print("What is the return value of type(B) is not float? \n",type(B) is not float)
        print("What is the return value of type(B) is not str? \n",type(B) is not str)

    elif EC == "8":#complement
        binary = input("Enter Binary:")
        l = len(binary)
        ones_com = ""
        for x in range(l):
            if binary[x] == "0" or binary[x] == "1":
                if binary[x] == "0":
                    a = "1" 
                elif binary[x]=='1': 
                    a = "0"
                ones_com = ones_com + a
            else:
                print("Invalid input")
                
        print("1's Complement:", ones_com)
        twos_com = ""
        b = 1
        for y in reversed(ones_com):
            if y == "1" and b == 1:
                twos_com = "0" + twos_com
            elif y == "0" and b == 1:
                twos_com = "1" + twos_com
                b = 0
            else:
                twos_com = y + twos_com
        print("2's Complement:", twos_com)
    main()
main()
        
