def main():
    print("[1]Domestic destination\n[2]International destination\n")
    kd=input("ENTER YOUR DESTINATION:")
    if kd =="1":
        print("[1]Cebu\n[2]Cagayan de oro\n[3]Laoag\n[4]Legaspi\n[5]Puerto rico")
        places={1:"Cebu",2:"Cagayan de oro",3:"Laoag",4:"legaspi",5:"Puerto rico"}
        prices={1:4275,2:5882,3:2937,4:6150,5:6401}
        discount={"0-1":0.10,"2-59":1,"60":.80}

        age=int(input("Enter age:"))
        code=int(input("Enter code[1-5]:"))

        if code > 5:
            print("invalid destination code\n")
        else:
            totalfare=prices[code]
            if age<=1:
                total=discount["0-1"]*totalfare
                print("Your airfare from Manila to ",str(places[code])+" is",str(total)+" pesos"+"\n")
            if age>=2 and age<=59:
                total=discount["2-59"]*totalfare
                print("Your airfare from  Manila to",str(places[code])+" is",str(total)+" pesos"+"\n")
            if age>=60:
                total=discount["60"]*totalfare
                print("Your airfare from Manila to ",str(places[code])+" is",str(total)+" pesos"+"\n")

    if kd=="2":
        print("[1]Singapore\n[2]Bangkok\n[3]Tokyo\n[4]Seoul\n[5]Taipei")
        places={1:"Singapore",2:"Bangkok",3:"Tokyo",4:"Seoul",5:"Taipei"}
        prices={1:4275,2:7795,3:10285,4:6150,5:8401}
        discount={"0-1":0.10,"2-59":1,"60":.80}

        age=int(input("Enter age:"))
        code=int(input("Enter code[1-5]:"))

        if code > 5:
            print("invalid destination code\n")
        else:
            totalfare=prices[code]
            if age<=1:
                total=discount["0-1"]*totalfare
                print("Your airfare from Manila to ",str(places[code])+" is",str(total)+" pesos"+"\n")
            if age>=2 and age<=59:
                total=discount["2-59"]*totalfare
                print("Your airfare from Manila to ",str(places[code])+" is",str(total)+" pesos"+"\n")
            if age>=60:
                total=discount["60"]*totalfare
                print("Your airfare from Manila to ",str(places[code])+" is",str(total)+" pesos"+"\n")
    main()
main()

        
