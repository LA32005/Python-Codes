def main():
   PR= float(input("Enter payrate:"))
   NHW=int(input("Enter number of hours work:"))
   EC=input("Enter employee's code(A OR B):")
   SC=input("Enter state code(Y OR J):")

   if NHW>=40:
      RG=NHW*40
      OT=1.5*((PR*1.5)*NHW)
   elif NHW<40:
      RG=NHW*PR
      OT=0

   GR=RG+OT

   if EC=="A" and SC=="J":
      TAX=GR*0.45
   elif EC=="A" and SC=="Y":
      TAX=GR*0.7
   elif EC=="B":
      TAX=0

   NP=GR-TAX

   print("REGULAR PAY:",(RG))
   print("OVERTIME:",(OT))
   print("TAX:", (TAX))
   print("GROSS PAY:", (GR))
   print("NETPAY:", (NP))
   main()
main()
