from tkinter import*
t=Tk()
t.title('Grading System')
Label(t,text="NAME").grid(row=0,sticky=W)#LABEL
Label(t,text="YR/SEC").grid(row=1,sticky=W)
name=Entry(t,bd=10)#GRID
sec=Entry(t,bd=10)

name.grid(row=0,column=1)
sec.grid(row=1,column=1)#POSITION

Label(t,text="PRELIM",bg="lightblue").grid(row=3,column=1)#LABEL
Label(t,text="QUIZ 1").grid(row=4,sticky=W)
Label(t,text="QUIZ 2").grid(row=5,sticky=W)
Label(t,text="ASSIGNMENT").grid(row=6,sticky=W)
Label(t,text="ATTENDANCE").grid(row=7,sticky=W)
Label(t,text="PROJECT").grid(row=8,sticky=W)
Label(t,text="SEATWORK").grid(row=9,sticky=W)
Label(t,text="MAJOR EXAM").grid(row=10,sticky=W)

pq1=Entry(t,bd=10)#GRID
pq2=Entry(t,bd=10)
passign=Entry(t,bd=10)
patt=Entry(t,bd=10)
pproj=Entry(t,bd=10)
pseat=Entry(t,bd=10)
pme=Entry(t,bd=10)



pq1.grid(row=4,column=1)#POSITION
pq2.grid(row=5,column=1)
passign.grid(row=6,column=1)
patt.grid(row=7,column=1)
pproj.grid(row=8,column=1)
pseat.grid(row=9,column=1)
pme.grid(row=10,column=1)


Label(t,text="MIDTERM",bg="lightblue").grid(row=3,column=2)#LABEL
mq1=Entry(t,bd=10)#GRID
mq2=Entry(t,bd=10)
massign=Entry(t,bd=10)
matt=Entry(t,bd=10)
mproj=Entry(t,bd=10)
mseat=Entry(t,bd=10)
mme=Entry(t,bd=10)


mq1.grid(row=4,column=2)#POSITION
mq2.grid(row=5,column=2)
massign.grid(row=6,column=2)
matt.grid(row=7,column=2)
mproj.grid(row=8,column=2)
mseat.grid(row=9,column=2)
mme.grid(row=10,column=2)



Label(t,text="FINALS",bg="lightblue").grid(row=3,column=3)#LABEL
fq1=Entry(t,bd=10)#GRID
fq2=Entry(t,bd=10)
fassign=Entry(t,bd=10)
fatt=Entry(t,bd=10)
fproj=Entry(t,bd=10)
fseat=Entry(t,bd=10)
fme=Entry(t,bd=10)


fq1.grid(row=4,column=3)#POSITION
fq2.grid(row=5,column=3)
fassign.grid(row=6,column=3)
fatt.grid(row=7,column=3)
fproj.grid(row=8,column=3)
fseat.grid(row=9,column=3)
fme.grid(row=10,column=3)

Label(t,text="NAME:").grid(row=12,sticky=W)
Label(t,text="YR/SEC:").grid(row=13,sticky=W)
Label(t,text="PRELIM GRADE:").grid(row=14,sticky=W)
Label(t,text="MIDTERM GRADE").grid(row=15,sticky=W)
Label(t,text="FINAL GRADE").grid(row=16,sticky=W)
Label(t,text="TOTAL").grid(row=17,sticky=W)
Label(t,text="LETTER GRADE:").grid(row=18,sticky=W)
Label(t,text="REMARKS:").grid(row=19,sticky=W)


def calculate():
    louis=name.get()
    na.set(louis)
    section=sec.get()
    year.set(section)
    pq=int(pq1.get())+int(pq2.get())#prelim
    paq=(pq/2)*0.40
    pcs=int(passign.get())+int(patt.get())+int(pproj.get())+int(pseat.get())
    pacs=(pcs/4)*0.10
    pmea=int(pme.get())*.50
    pg=paq+pacs+pmea
    mypg.set(pg)

    mq=int(pq1.get())+int(pq2.get())#midterm
    maq=(mq/2)*0.40
    mcs=int(massign.get())+int(matt.get())+int(mproj.get())+int(mseat.get())
    macs=(mcs/4)*0.10
    mmea=int(mme.get())*.50
    mg=maq+macs+mmea
    mymg.set(mg)

    fq=int(fq1.get())+int(fq2.get())#finals
    faq=(fq/2)*0.40
    fcs=int(fassign.get())+int(fatt.get())+int(fproj.get())+int(fseat.get())
    facs=(fcs/4)*0.10
    fmea=int(fme.get())*.50
    fg=faq+facs+fmea
    myfg.set(fg)

    tg = (pg+mg+fg)/3
    mytg.set(tg)
    

    if (float(tg) >= 95):
        letter="A+"
        let.set(letter)
        stat="PASSED"
        status.set(stat)
      
    elif (float(tg) >= 90) and (float(tg) <= 94):
        letter="A"
        let.set(letter)
        stat="PASSED"
        status.set(stat)
    elif (float(tg) >= 85) and (float(tg) <= 89):
        letter="A-"
        let.set(letter)
        stat="PASSED"
        status.set(stat)
    elif (float(tg) >= 80) and (float(tg) <=84):
        letter="B+"
        let.set(letter)
        stat="PASSED"
        status.set(stat)
    elif (float(tg) >= 78) and (float(tg) <=  79):
        letter="B"
        let.set(letter)
        stat="PASSED"
        status.set(stat)
    elif (float(tg) >= 75) and (float(tg) <= 77):
        letter="B-"
        let.set(letter)
    elif (float(tg) <= 74):
        letter="C"
        let.set(letter)
        stat="FAILED"
        status.set(stat)
na=StringVar()
year=StringVar()
mypg=StringVar()
mymg=StringVar()
myfg=StringVar()
mytg=StringVar()
let=StringVar()
status=StringVar()
#RESULT
result_name=Label(t,text='',textvariable=na).grid(row=12,column=1,sticky=W)
section_result=Label(t,text='',textvariable=year).grid(row=13,column=1,sticky=W)
pg_result=Label(t,text='',textvariable=mypg).grid(row=14,column=1,sticky=W)
mg_result=Label(t,text='',textvariable=mymg).grid(row=15,column=1,sticky=W)
fg_result=Label(t,text='',textvariable=myfg).grid(row=16,column=1,sticky=W)
tg_RESULT=Label(t,text='',textvariable=mytg).grid(row=17,column=1,sticky=W)
lettergrade_result=Label(t,text='',textvariable=let).grid(row=18,column=1,sticky=W)
remark_result=Label(t,text='',textvariable=status).grid(row=19,column=1,sticky=W)

b=Button(t,text="CALCULATE",command=calculate,bg="green",bd=10)
b.grid(row=11,column=0,sticky=W+E+N+S,padx=5,pady=5)
t.mainloop()

