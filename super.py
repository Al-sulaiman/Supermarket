from tkinter import *
import math , random , os
from tkinter import messagebox
from tkinter import font
class super:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1200x800+10+10')
        self.root.title('Super market ')
        self.root.resizable(False,False)
        self.root.iconbitmap('C:\\Users\\KIIT\\Downloads\\i.ico')
        title=Label(self.root,text='project managmnet:super market',fg='white',bg='#0B2F3A',font=('tajawal',13))
        title.pack(fill=X)
        #================variable===========
        #====================البقوليات q1,q18===============
        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        self.q7=IntVar()
        self.q8=IntVar()
        self.q9=IntVar()
        self.q10=IntVar()
        self.q11=IntVar()
        self.q12=IntVar()
        self.q13=IntVar()
        self.q14=IntVar()
        self.q15=IntVar()
        self.q16=IntVar()
        self.q17=IntVar()
        self.q18=IntVar()
        #===============اللوازم المنزليةqq1,qq18=============
        self.qq1=IntVar()
        self.qq2=IntVar()
        self.qq3=IntVar()
        self.qq4=IntVar()
        self.qq5=IntVar()
        self.qq6=IntVar()
        self.qq7=IntVar()
        self.qq8=IntVar()
        self.qq9=IntVar()
        self.qq10=IntVar()
        self.qq11=IntVar()
        self.qq12=IntVar()
        self.qq13=IntVar()
        self.qq14=IntVar()
        self.qq15=IntVar()
        self.qq16=IntVar()
        self.qq17=IntVar()
        self.qq18=IntVar()
        #===============الادوات الكهرباءqqq1,qqq15===============
        self.qqq1=IntVar()
        self.qqq2=IntVar()
        self.qqq3=IntVar()
        self.qqq4=IntVar()
        self.qqq5=IntVar()
        self.qqq6=IntVar()
        self.qqq7=IntVar()
        self.qqq8=IntVar()
        self.qqq9=IntVar()
        self.qqq10=IntVar()
        self.qqq11=IntVar()
        self.qqq12=IntVar()
        self.qqq13=IntVar()
        self.qqq14=IntVar()
        self.qqq15=IntVar()
        #=====================متغيرات بيانات المشتري===========
        self.namo=StringVar()
        self.phono=StringVar()

        self.fatora=StringVar()
        x=random.randint(1000,9999)
        self.fatora.set(str(x))
        #===================متغيرات الجساب الكلي================ 
        self.bocl=StringVar()
        self.adoat=StringVar()
        self.kahraba=StringVar()
        #=====customer data==========
        f1=Frame(root,bd=2,width=338,height=170,bg='#0B4C5F')
        f1.place(x=880,y=25)
        tit=Label(f1,text=':بيانات المشتري',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='tomato')
        tit.place(x=190,y=0)
       
        his_name=Label(f1,text=':اسم المشتري',font=('tajawal',10,'bold',),bg='#0B4C5F',fg='white')
        his_name.place(x=220,y=40)
        his_phone=Label(f1,text=':رقم المشتري',font=('tajawal',10,'bold',),bg='#0B4C5F',fg='white')
        his_phone.place(x=225,y=80)
        bill_num=Label(f1,text=':رقم الفاتورة',font=('tajawal',10,'bold',),bg='#0B4C5F',fg='white')
        bill_num.place(x=242,y=120)
 
        en_name=Entry(f1,justify='center',textvariable=self.namo)
        en_name.place(x=90,y=42)
        en_phone=Entry(f1,justify='center',textvariable=self.phono)
        en_phone.place(x=90,y=78)
        en_bill=Entry(f1,justify='center',textvariable=self.fatora)
        en_bill.place(x=90,y=120)

        btn_customer=Button(f1,text='بحث',font=('tajawal',10),width=8,height=4,bg='white')
        btn_customer.place(x=3,y=40)
        #========bill =============
        l=Label(f1,text='[الفواتير]',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='gold')
        l.place(x=125,y=145)
        f3=Frame(root,bd=2,width=338,height=390,bg='white')
        f3.place(x=879,y=195)

        scrol_y=Scrollbar(f3,orient=VERTICAL)
        self.textarea=Text(f3,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        #===========price============
        f4=Frame(root,bd=2,width=657,height=112,bg='#0B4C5F')
        f4.place(x=640,y=580)
        hesab=Button(f4,text='الحساب',width=13,height=1,font='tajawal',bg='#DBA901',command=self.total)
        hesab.place(x=430,y=10)
        bil=Button(f4,text='تصدير الفاتورة',width=13,height=1,font='tajawal',bg='#DBA901')
        bil.place(x=430,y=50)
        clear=Button(f4,text='افراغ الحقول',width=13,height=1,font='tajawal',bg='#DBA901')
        clear.place(x=310,y=10)
        ex=Button(f4,text='اغلاق البرنامج',width=13,height=1,font='tajawal',bg='#DBA901')
        ex.place(x=310,y=50)
        lbl=Label(f4,text='حساب الكلي للبقوليات',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lbl.place(x=170,y=10)
        lbl2=Label(f4,text='حساب اللوازم المنزلية',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lbl2.place(x=170,y=40)
        lbl3=Label(f4,text='حساب اللوازم الكهرباء',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lbl3.place(x=170,y=70)


        ento1=Entry(f4,width=20,textvariable=self.bocl)
        ento1.place(x=40,y=12)

        ento2=Entry(f4,width=20,textvariable=self.adoat)
        ento2.place(x=40,y=40)

        ento3=Entry(f4,width=20,textvariable=self.kahraba)
        ento3.place(x=40,y=70)
        #===========items[1]=============
        ff1=Frame(root,bd=2,width=318,height=664,bg='#0B4C5F')  
        ff1.place(x=1,y=27)  
        t=Label(ff1,text='البقوليات',font=('tajawal',12,'bold'),bg='#0B4C5F', fg='gold')
        t.place(x=122,y=0)
        bq1=Label(ff1,text='الارز',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq1.place(x=250,y=40)

        bq2=Label(ff1,text='برغل',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq2.place(x=250,y=70)

        bq3=Label(ff1,text='قاصولياء',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq3.place(x=230,y=100)

        bq4=Label(ff1,text='عدس',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq4.place(x=250,y=130)

        bq5=Label(ff1,text='معكرونة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq5.place(x=240,y=160)

        bq6=Label(ff1,text='فريكة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq6.place(x=240,y=190)

        bq7=Label(ff1,text='حمص',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq7.place(x=240,y=220)

        bq8=Label(ff1,text='فول',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq8.place(x=250,y=250)

        bq9=Label(ff1,text='ملج',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq9.place(x=250,y=280)

        bq10=Label(ff1,text='سكر',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq10.place(x=250,y=310)

        bq11=Label(ff1,text='فلقل اسود',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq11.place(x=220,y=340)

        bq12=Label(ff1,text='فلفل احمر',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq12.place(x=220,y=370)

        bq13=Label(ff1,text='اللوبيا',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq13.place(x=240,y=400)

        bq14=Label(ff1,text='الادمامي',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq14.place(x=230,y=430)

        bq15=Label(ff1,text='الثمح',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq15.place(x=245,y=460)

        bq16=Label(ff1,text='الشعير',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq16.place(x=240,y=490)

        bq17=Label(ff1,text='الشوفان',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq17.place(x=230,y=520)

        bq18=Label(ff1,text='الذرة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bq18.place(x=245,y=550)

          #================انشاء حقول ادخال==========
        
        bqent1=Entry(ff1,width=12,textvariable=self.q1)
        bqent1.place(x=70,y=40)

        bqent2=Entry(ff1,width=12,textvariable=self.q2)
        bqent2.place(x=70,y=70)

        bqent3=Entry(ff1,width=12,textvariable=self.q3)
        bqent3.place(x=70,y=100)

        bqent4=Entry(ff1,width=12,textvariable=self.q4)
        bqent4.place(x=70,y=130)

        bqent5=Entry(ff1,width=12,textvariable=self.q5)
        bqent5.place(x=70,y=160)

        bqent6=Entry(ff1,width=12,textvariable=self.q6)
        bqent6.place(x=70,y=190)

        bqent7=Entry(ff1,width=12,textvariable=self.q7)
        bqent7.place(x=70,y=220)

        bqent8=Entry(ff1,width=12,textvariable=self.q8)
        bqent8.place(x=70,y=250)

        bqent9=Entry(ff1,width=12,textvariable=self.q9)
        bqent9.place(x=70,y=280)

        bqent10=Entry(ff1,width=12,textvariable=self.q10)
        bqent10.place(x=70,y=310)

        bqent11=Entry(ff1,width=12,textvariable=self.q11)
        bqent11.place(x=70,y=340)

        bqent12=Entry(ff1,width=12,textvariable=self.q12)
        bqent12.place(x=70,y=370)

        bqent13=Entry(ff1,width=12,textvariable=self.q13)
        bqent13.place(x=70,y=400)

        bqent14=Entry(ff1,width=12,textvariable=self.q14)
        bqent14.place(x=70,y=430)

        bqent15=Entry(ff1,width=12,textvariable=self.q15)
        bqent15.place(x=70,y=460)

        bqent16=Entry(ff1,width=12,textvariable=self.q16)
        bqent16.place(x=70,y=490)

        bqent17=Entry(ff1,width=12,textvariable=self.q17)
        bqent17.place(x=70,y=520)

        bqent18=Entry(ff1,width=12,textvariable=self.q18)
        bqent18.place(x=70,y=550)

        #============items[2]========
       
        ff2=Frame(root,bd=2,width=318,height=664,bg='#0B4C5F')  
        ff2.place(x=321,y=27)
          
        tt=Label(ff2,text='اللوازم المنزلية',font=('tajawal',12,'bold'),bg='#0B4C5F', fg='gold')
        tt.place(x=122,y=0)
        bqr1=Label(ff2,text='مصفاة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr1.place(x=250,y=40)

        bqr2=Label(ff2,text='صحن',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr2.place(x=250,y=70)

        bqr3=Label(ff2,text='كأس',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr3.place(x=250,y=100)

        bqr4=Label(ff2,text='ابريق',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr4.place(x=250,y=130)

        bqr5=Label(ff2,text='سكين',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr5.place(x=250,y=160)

        bqr6=Label(ff2,text='شوك',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr6.place(x=250,y=190)

        bqr7=Label(ff2,text='طنجرة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr7.place(x=250,y=220)

        bqr8=Label(ff2,text='سلة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr8.place(x=250,y=250)

        bqr9=Label(ff2,text='ملاعق',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr9.place(x=250,y=280)

        bqr10=Label(ff2,text='صينية',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr10.place(x=250,y=310)

        bqr11=Label(ff2,text='وعاء',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr11.place(x=250,y=340)

        bqr12=Label(ff2,text='علب',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr12.place(x=250,y=370)

        bqr13=Label(ff2,text='مقشرة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr13.place(x=250,y=400)

        bqr14=Label(ff2,text='لوح تقطيع',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr14.place(x=230,y=430)

        bqr15=Label(ff2,text='قشارة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr15.place(x=245,y=460)

        bqr16=Label(ff2,text='سلة قمامة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr16.place(x=230,y=490)

        bqr17=Label(ff2,text='منفضة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr17.place(x=240,y=520)

        bqr18=Label(ff2,text='أكياس',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqr18.place(x=245,y=550)

          #================انشاء حقول ادخال==========
        
        bqen1=Entry(ff2,width=12,textvariable=self.qq1)
        bqen1.place(x=70,y=40)

        bqen2=Entry(ff2,width=12,textvariable=self.qq2)
        bqen2.place(x=70,y=70)

        bqen3=Entry(ff2,width=12,textvariable=self.qq3)
        bqen3.place(x=70,y=100)

        bqen4=Entry(ff2,width=12,textvariable=self.qq4)
        bqen4.place(x=70,y=130)

        bqen5=Entry(ff2,width=12,textvariable=self.qq5)
        bqen5.place(x=70,y=160)

        bqen6=Entry(ff2,width=12,textvariable=self.qq6)
        bqen6.place(x=70,y=190)

        bqen7=Entry(ff2,width=12,textvariable=self.qq7)
        bqen7.place(x=70,y=220)

        bqen8=Entry(ff2,width=12,textvariable=self.qq8)
        bqen8.place(x=70,y=250)

        bqen9=Entry(ff2,width=12,textvariable=self.qq9)
        bqen9.place(x=70,y=280)

        bqen10=Entry(ff2,width=12,textvariable=self.qq10)
        bqen10.place(x=70,y=310)

        bqen11=Entry(ff2,width=12,textvariable=self.qq11)
        bqen11.place(x=70,y=340)

        bqen12=Entry(ff2,width=12,textvariable=self.qq12)
        bqen12.place(x=70,y=370)

        bqen13=Entry(ff2,width=12,textvariable=self.qq13)
        bqen13.place(x=70,y=400)

        bqen14=Entry(ff2,width=12,textvariable=self.qq14)
        bqen14.place(x=70,y=430)

        bqen15=Entry(ff2,width=12,textvariable=self.qq15)
        bqen15.place(x=70,y=460)

        bqen16=Entry(ff2,width=12,textvariable=self.qq16)
        bqen16.place(x=70,y=490)

        bqen17=Entry(ff2,width=12,textvariable=self.qq17)
        bqen17.place(x=70,y=520)

        bqen18=Entry(ff2,width=12,textvariable=self.qq18)
        bqen18.place(x=70,y=550)

   #==============items[3]===============

        ff3=Frame(root,bd=2,width=238,height=550,bg='#0B4C5F')  
        ff3.place(x=640,y=27)


        ttt=Label(ff3,text='الادوات الكهرباء',font=('tajawal',12,'bold'),bg='#0B4C5F', fg='gold')
        ttt.place(x=122,y=0)
        bqrr1=Label(ff3,text='مكنسة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr1.place(x=180,y=40)

        bqrr2=Label(ff3,text='غسالة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr2.place(x=180,y=70)

        bqrr3=Label(ff3,text='براد',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr3.place(x=180,y=100)

        bqrr4=Label(ff3,text='مكواة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr4.place(x=180,y=130)

        bqrr5=Label(ff3,text='سخان',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr5.place(x=180,y=160)

        bqrr6=Label(ff3,text='جلاية',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr6.place(x=180,y=190)

        bqrr7=Label(ff3,text='شاحن',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr7.place(x=180,y=220)

        bqrr8=Label(ff3,text='مروحة ارضية',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr8.place(x=160,y=250)

        bqrr9=Label(ff3,text='مروحة سقفية',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr9.place(x=160,y=280)

        bqrr10=Label(ff3,text='شاشة42',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr10.place(x=170,y=310)

        bqrr11=Label(ff3,text='شاشة32',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr11.place(x=170,y=340)

        bqrr12=Label(ff3,text='خلاط',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr12.place(x=180,y=370)

        bqrr13=Label(ff3,text='مكنسة',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr13.place(x=180,y=400)

        bqrr14=Label(ff3,text='فلتر ماء',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr14.place(x=180,y=430)

        bqrr15=Label(ff3,text='فرن غاز',font=('tajawal',11,'bold'),bg='#0B4C5F',fg='white')
        bqrr15.place(x=180,y=460)

           #================انشاء حقول ادخال==========
        
        bqe1=Entry(ff3,width=12,textvariable=self.qqq1)
        bqe1.place(x=70,y=40)

        bqe2=Entry(ff3,width=12,textvariable=self.qqq2)
        bqe2.place(x=70,y=70)

        bqe3=Entry(ff3,width=12,textvariable=self.qqq3)
        bqe3.place(x=70,y=100)

        bqe4=Entry(ff3,width=12,textvariable=self.qqq4)
        bqe4.place(x=70,y=130)

        bqe5=Entry(ff3,width=12,textvariable=self.qqq5)
        bqe5.place(x=70,y=160)

        bqe6=Entry(ff3,width=12,textvariable=self.qqq6)
        bqe6.place(x=70,y=190)

        bqe7=Entry(ff3,width=12,textvariable=self.qqq7)
        bqe7.place(x=70,y=220)

        bqe8=Entry(ff3,width=12,textvariable=self.qqq8)
        bqe8.place(x=70,y=250)

        bqe9=Entry(ff3,width=12,textvariable=self.qqq9)
        bqe9.place(x=70,y=280)

        bqe10=Entry(ff3,width=12,textvariable=self.qqq10)
        bqe10.place(x=70,y=310)

        bqe11=Entry(ff3,width=12,textvariable=self.qqq11)
        bqe11.place(x=70,y=340)

        bqe12=Entry(ff3,width=12,textvariable=self.qqq12)
        bqe12.place(x=70,y=370)

        bqe13=Entry(ff3,width=12,textvariable=self.qqq13)
        bqe13.place(x=70,y=400)

        bqe14=Entry(ff3,width=12,textvariable=self.qqq14)
        bqe14.place(x=70,y=430)

        bqe15=Entry(ff3,width=12,textvariable=self.qqq15)
        bqe15.place(x=70,y=460)
        
    def total(self):
        self.rez=self.q1.get()*1.5
        self.bergl=self.q2.get()*1.5
        self.a=self.q3.get()*2
        self.b=self.q4.get()*2
        self.c=self.q5.get()*2  
        self.d=self.q6.get()*2
        self.e=self.q7.get()*2
        self.f=self.q8.get()*2
        self.g=self.q9.get()*2
        self.h=self.q10.get()*2
        self.m=self.q11.get()*2
        self.p=self.q12.get()*2
        self.q=self.q13.get()*2
        self.r=self.q14.get()*2
        self.t=self.q15.get()*2
        self.o=self.q16.get()*2
        self.l=self.q17.get()*2                   
        self.n=self.q18.get()*2 
        self.totall=float(
          self.rez+
          self.bergl+
          self.a+
          self.b+
          self.l+
          self.r+
          self.t+
          self.e+
          self.c+
          self.f+
          self.o+
          self.n+
          self.q+
          self.h+
          self.p+
          self.g+
          self.m+
          self.d
          )
        self.bocl.set(str(self.totall)+" $ ")  


        self.welcome() 

    def welcome(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tسوبر ماركت الخبير يرحب بكم")
        self.textarea.insert(END,"\n==========================")
        self.textarea.insert(END,f"\n\t B.NUM :{self.fatora.get()}")
        self.textarea.insert(END,f"\n\t NAMR  :{self.namo.get()}")
        self.textarea.insert(END,f"\n\tPHONE  :{self.phono.get()}")
        self.textarea.insert(END,"\n==========================")
        self.textarea.insert(END,f"\nالسعر\t      العدد \t      المشتريات")
        self.textarea.insert(END,"\n==========================")
       

      

root=Tk()
ob=super(root)
root.mainloop()