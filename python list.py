L1=[]
L2=[]
L3=[]
def main():
    nosr=int(input("Number of Student Record"))
    for x in range(nosr):
        Id=int(input("Enter student id:"))
        name=input("Enter student name:")
        grade=int(input("Enter student Grade:"))
        print("\n")
        L1.append(Id)
        L2.append(name)
        L3.append(grade)
    print("Display All Record")
    print("Student ID\tStudent Name\tStudent Grade")
    print(L1,"\t",end="")
    print(L2,"\t",end="")
    print(L3,"\t")

    print("Select record to delete")
    ind=int(input("Enter the index position to delete:"))
    L1.remove(L1[ind])
    L2.remove(L2[ind])
    L3.remove(L3[ind])
    print("Student ID\tStudent Name\tStudent Grade")
    print(L1,"\t",end="")
    print(L2,"\t",end="")
    print(L3,"\t")

    print("Insert record")    
    ind=int(input("Enter the index position to insert record:"))
    new_Id=int(input("Enter New id:"))
    new_name=input("Enter New student name:")
    new_grade=int(input("Enter New student Grade:"))

    L1.insert(ind,new_Id)
    L2.insert(ind,new_name)
    L3.insert(ind,new_grade)
    print("Student ID\tStudent Name\tStudent Grade")
    print(L1,"\t",end="")
    print(L2,"\t",end="")
    print(L3,"\t")
    main()
main()
    
    
        

    
    
    
    
