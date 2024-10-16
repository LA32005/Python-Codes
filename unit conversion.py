def main():
    print("[1] Farenheit to Celcius\n[2] Celcius to Farenheit\n[3] Celcius to Kelvin\n[4] Kelvin to Farenheit\n[5] Farenheit to kelvin\n[6]kelvin to celcius")
    scu=input("Enter unit conversion:")

    if scu=="1":
        f=float(input("Enter Farenheit:"))
        c=(f-32)*5/9
        print(str(c)+"°C")

    if scu=="2":
        c=float(input("Enter celcius:"))
        f=(c*9/5)+32
        print(str(f) + "°F")

    if scu=="3":
        c=float(input("Enter celcius:"))
        k=c+273.15
        print(str(k) + "k")

    if scu=="4":
        k=float(input("Enter kelvin:"))
        f=(k-273.15)*9/5+32
        print(str(f) +"°F")

    if scu=="5":
        f=float(input("Enter farenheit:"))
        k=(f-32)*5/9+273.15
        print(str(k) + "k")

    if scu=="6":
        k=float(input("Enter kelvin:"))
        c=k-273.15
        print(str(c) + "°C")
    main()
main()
