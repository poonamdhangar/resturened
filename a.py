from faulthandler import disable
from tkinter import *
from tkinter import messagebox

# Create the function
def main():
    # Create Tk object
    root= Tk()
    app=LoginPage(root)
    root.mainloop()
class LoginPage:
    def __init__(self,root):
        self.root=root
        self.root.title("poonam")
        self.label=Label(text="Resturant Managment System",font=('Arial',35,'bold'),bg="lightgray",bd=8,relief=GROOVE)
        self.label.pack(side=TOP,fill=X)
        self.main_frame=Frame(self.root,bg="lightgray",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=450)
        self.login_lbl=Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="lightgray",font=('Arial',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)
        #  Enter the Details 
        
        self.entry_frame=LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="lightgray",font=('Arial',18))
        self.entry_frame.pack(fill=BOTH,expand=True)
        # variable create 
        username=StringVar()
        password=StringVar()
        self.entry_lbl=Label(self.entry_frame,text="Enter Username:",bg="lightgray",font=('Arial',15))
        self.entry_lbl.grid(row=0,column=0)
        self.entry_ent=Entry(self.entry_frame,font=('Arial',15),bd=6,textvariable=username)
        self.entry_ent.grid(row=0,column=1,pady=2,padx=2)
        # Password Fields
        self.password_lbl=Label(self.entry_frame,text="Entry Password:",bg="lightgray",font=('Arial',15))
        self.password_lbl.grid(row=1,column=0)
        self.password_ent=Entry(self.entry_frame,font=('Arial',15),bd=6,textvariable=password,show="*")
        self.password_ent.grid(row=1,column=1,pady=2,padx=2)
        
        # Button ***********
        # ***********************Functions ***********
        def check_login():
            if username.get()=="" and password.get()=="":
                self.bil_button.config(state="normal")
                pass
            else:
                messagebox.showwarning("Error","Please enter the right username")
                pass
        def reset():
            username.set("")
            password.set("")
        def billing_seet():
            self.newwindow=Toplevel(self.root)
            self.app=window2(self.newwindow)
            
        self.button_frame=LabelFrame(self.entry_frame,text="Option",font=("Arial",20,'bold'),bg="lightgray",relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)
        
        self.login_button=Button(self.button_frame,text="Login",font=('Arial',15),bd=5,width=15,command=check_login)
        self.login_button.grid(row=0,column=0,pady=2,padx=40)
        
        self.bil_button=Button(self.button_frame,text="Billing",font=('Arial',15),bd=5,width=15,command=billing_seet)
        self.bil_button.grid(row=0,column=1,pady=2,padx=40)
        
        self.bil_button.config(state="disabled")
        
        self.reset_button=Button(self.button_frame,text="Reset",font=('Arial',15),bd=5,width=15,command=reset)
        self.reset_button.grid(row=0,column=2,pady=2,padx=20)
        pass
class window2:
    def __init__(self,root):
        self.root=root
        self.root.title("poonam")
        self.root.geometry('1350x720')
        self.label=Label(self.root,text="Resturant Managment System",font=('Arial',35,'bold'),bg="lightgray",bd=8,relief=GROOVE)
        self.label.pack(side=TOP,fill=X)
        import random
        bill_no=random.randint(1,100)
        bil_no_value=IntVar()
        bil_no_value.set(bill_no)
        self.entry_frame=LabelFrame(self.root,text="Enter Details",bd=6,relief=GROOVE,bg="lightgray",font=('Arial',18))
        self.entry_frame.place(x=20,y=95,width=500,height=650)
        #  Bil Number
        self.bill_no=Label(self.entry_frame,text="Bill Number",bg="lightgray",font=('Arial',15))
        self.bill_no.grid(row="0",column="0",pady=2,padx=2)
        
        
        self.bil_entry=Entry(self.entry_frame,font=('Arial',15),bd=6,textvariable=bil_no_value)
        self.bil_entry.grid(row=0,column=1,pady=2,padx=2)
        
        #  Bil Number
        self.customer_name=Label(self.entry_frame,text="Customer Name",bg="lightgray",font=('Arial',15))
        self.customer_name.grid(row=1,column=0,pady=2,padx=2)
        
        self.customer_name_entry=Entry(self.entry_frame,font=('Arial',15),bd=6)
        self.customer_name_entry.grid(row=1,column=1,pady=2,padx=2)
    
        #  Bil Number
        self.customer_contact=Label(self.entry_frame,text="Customer Contact",bg="lightgray",font=('Arial',15))
        self.customer_contact.grid(row=2,column=0,pady=2,padx=2)
        
        self.customer_contact_entry=Entry(self.entry_frame,font=('Arial',15),bd=6)
        self.customer_contact_entry.grid(row=2,column=1,pady=2,padx=2)
        # Date
        self.date=Label(self.entry_frame,text="Date",bg="lightgray",font=('Arial',15))
        self.date.grid(row=3,column=0,pady=2,padx=2)
        
        self.date_entry=Entry(self.entry_frame,font=('Arial',15),bd=6)
        self.date_entry.grid(row=3,column=1,pady=2,padx=2)
        
        self.items_purchased=Label(self.entry_frame,text="Items Purchased",bg="lightgray",font=('Arial',15))
        self.items_purchased.grid(row=4,column=0,pady=2,padx=2)
        
        self.item_purchased_entry=Entry(self.entry_frame,font=('Arial',15),bd=6)
        self.item_purchased_entry.grid(row=4,column=1,pady=2,padx=2)
        # Items Quantity
        self.item_quantity=Label(self.entry_frame,text="Items Quantity",bg="lightgray",font=('Arial',15))
        self.item_quantity.grid(row=5,column=0,pady=2,padx=2)
        
        self.item_quantity_entry=Entry(self.entry_frame,font=('Arial',15),bd=6)
        self.item_quantity_entry.grid(row=5,column=1,pady=2,padx=2)
        # Cost Of One
        self.cost_of_one=Label(self.entry_frame,text="Cost of One",bg="lightgray",font=('Arial',15))
        self.cost_of_one.grid(row=6,column=0,pady=2,padx=2)
        
        self.cost_of_one_entry=Entry(self.entry_frame,font=('Arial',15),bd=6)
        self.cost_of_one_entry.grid(row=6,column=1,pady=2,padx=2)
        
        
        #================Buttom============
        self.button_frame=LabelFrame(self.entry_frame,bd=5,text="Option",bg="lightgray",font=('Arial',15))
        self.button_frame.place(x=20,y=390,width=450,height=500)
        
        self.add_btn=Button(self.button_frame,text="Add",bd=2,font=('Arial',12),width=12,height=3)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)
        
        self.generate=Button(self.button_frame,text="Generate",bd=2,font=('Arial',12),width=12,height=3)
        self.generate.grid(row=0,column=1,padx=4,pady=2)
        
        self.clear=Button(self.button_frame,text="Clear",bd=2,font=('Arial',12),width=15,height=3)
        self.clear.grid(row=0,column=2,padx=4,pady=2)
        
        self.total=Button(self.button_frame,text="Total",bd=2,font=('Arial',12),width=15,height=3)
        self.total.grid(row=1,column=0,padx=4,pady=2)
        
        self.reset=Button(self.button_frame,text="Reset",bd=2,font=('Arial',12),width=15,height=3)
        self.reset.grid(row=1,column=1,padx=4,pady=2)
        
        self.save=Button(self.button_frame,text="Save",bd=2,font=('Arial',12),width=15,height=3)
        self.save.grid(row=1,column=2,padx=4,pady=2)
        
        cal_var=StringVar
        
        #=====================Calculater================
        
        self.cal_frame=Frame(self.root,bd=8,background="lightgray",relief=GROOVE)
        self.cal_frame.place(x=570,y=110,width=680,height=295)
        
        self.num_ent=Entry(self.cal_frame,bd=15,background="lightgray",font=('Arial',15),width=57,justify=RIGHT,textvariable=cal_var)
        self.num_ent.grid(row=0,column=0,columnspan=11)
        
        def press_btn(event):
            text=event.widget.cget("text")
            if text=="=":
                if cal_var.get().isdigit():
                    value=int(cal_var.get())
                else:
                    try:
                        value=eval(self.num_ent.get())
                    except:
                        print("Error")
                cal_var.set(value)
                self.num_ent.update()
            elif text=="C":
                pass
            else:
                cal_var.set(cal_var.get()+ text)
                self.num_ent.update()
                
                pass
            
            
        self.btn7=Button(self.cal_frame,bg="lightgray",text="7",bd=8,width=12,height=1,font=('Arial',15))
        self.btn7.grid(row=1,column=0,pady=2,padx=2)
        self.btn7.bind("<Button-1>",press_btn)
        
        self.btn8=Button(self.cal_frame,bg="lightgray",text="8",bd=8,width=12,height=1,font=('Arial',15))
        self.btn8.grid(row=1,column=1,pady=2,padx=2)
        self.btn8.bind("<Button-1>",press_btn)
        self.btn9=Button(self.cal_frame,bg="lightgray",text="9",bd=8,width=12,height=1,font=('Arial',15))
        self.btn9.grid(row=1,column=2,pady=2,padx=2)
        self.btn9.bind("<Button-1>",press_btn)
        
        self.btnadd=Button(self.cal_frame,bg="lightgray",text="+",bd=8,width=12,height=1,font=('Arial',15))
        self.btnadd.grid(row=1,column=3,pady=2,padx=2)
        self.btnadd.bind("<Button-1>",press_btn)
        
        self.btn4=Button(self.cal_frame,bg="lightgray",text="4",bd=8,width=12,height=1,font=('Arial',15))
        self.btn4.grid(row=2,column=0,pady=2,padx=2)
        self.btn4.bind("<Button-1>",press_btn)
        
        self.btn5=Button(self.cal_frame,bg="lightgray",text="5",bd=8,width=12,height=1,font=('Arial',15))
        self.btn5.grid(row=2,column=1,pady=2,padx=2)
        self.btn5.bind("<Button-1>",press_btn)
        
        self.btn6=Button(self.cal_frame,bg="lightgray",text="6",bd=8,width=12,height=1,font=('Arial',15))
        self.btn6.grid(row=2,column=2,pady=2,padx=2)
        self.btn6.bind("<Button-1>",press_btn)
        
        self.btnsub=Button(self.cal_frame,bg="lightgray",text="-",bd=8,width=12,height=1,font=('Arial',15))
        self.btnsub.grid(row=2,column=3,pady=2,padx=2)
        self.btnsub.bind("<Button-1>",press_btn)
        
        self.btn1=Button(self.cal_frame,bg="lightgray",text="1",bd=8,width=12,height=1,font=('Arial',15))
        self.btn1.grid(row=3,column=0,pady=2,padx=2)
        self.btn1.bind("<Button-1>",press_btn)
        
        self.btn2=Button(self.cal_frame,bg="lightgray",text="2",bd=8,width=12,height=1,font=('Arial',15))
        self.btn2.grid(row=3,column=1,pady=2,padx=2)
        self.btn2.bind("<Button-1>",press_btn)
        self.btn3=Button(self.cal_frame,bg="lightgray",text="3",bd=8,width=12,height=1,font=('Arial',15))
        self.btn3.grid(row=3,column=2,pady=2,padx=2)
        self.btn3.bind("<Button-1>",press_btn)
        
        self.btnmul=Button(self.cal_frame,bg="lightgray",text="*",bd=8,width=12,height=1,font=('Arial',15))
        self.btnmul.grid(row=3,column=3,pady=2,padx=2)
        self.btnmul.bind("<Button-1>",press_btn)
        
        self.btn0=Button(self.cal_frame,bg="lightgray",text="0",bd=8,width=12,height=1,font=('Arial',15))
        self.btn0.grid(row=4,column=0,pady=2,padx=2)
        self.btn0.bind("<Button-1>",press_btn)
        
        self.btnpoint=Button(self.cal_frame,bg="lightgray",text=".",bd=8,width=12,height=1,font=('Arial',15))
        self.btnpoint.grid(row=4,column=1,pady=2,padx=2)
        self.btnpoint.bind("<Button-1>",press_btn)
        
        self.btnclear=Button(self.cal_frame,bg="lightgray",text="=",bd=8,width=12,height=1,font=('Arial',15))
        self.btnclear.grid(row=4,column=2,pady=2,padx=2)
        self.btnclear.bind("<Button-1>",press_btn)
        
        self.btndiv=Button(self.cal_frame,bg="lightgray",text="/",bd=8,width=12,height=1,font=('Arial',15))
        self.btndiv.grid(row=4,column=3,pady=2,padx=2)
        self.btndiv.bind("<Button-1>",press_btn)
        
        
        self.bill_frame=LabelFrame(self.root,text="Bill Area",font=('Arial',15),background="lightgray",relief=GROOVE,bd=8)
        self.bill_frame.place(x=585,y=420,width=650,height=320)
        
        self.y_scroll=Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt=Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=True)
        
        
    
if __name__=="__main__":
    main()
    