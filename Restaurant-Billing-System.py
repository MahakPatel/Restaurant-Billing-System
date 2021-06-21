from tkinter import *
import random
import time;
root = Tk()


def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    textinput.set(operator)

def btnclrardisplay():
    global operator
    operator=""
    textinput.set("")

def btnEqual():
    global operator
    sumup=str(eval(operator))
    textinput.set(sumup)
    operator=""
def Ref():
    x=random.randint(1,100)
    randomRef=str(x)
    ramd.set(randomRef)

    CoF=float(Fries.get())
    CoD = float(Drinks.get())
    CoP = float(Pizza.get())
    CoChickB = float(Chicken_Burger.get())
    CoCheeseB = float(Cheese_Burger.get())
    CoB=float( Burger.get())

    costofFries = CoF * 70
    costofDrinks = CoD * 50
    costofPizza = CoP * 150
    costofChickBurger = CoChickB * 200
    costofCheeseBurger = CoCheeseB * 180
    costofBurger = CoB * 110

    CostofMeal = str('%.2f' % (costofFries + costofDrinks + costofPizza + costofChickBurger + costofCheeseBurger + costofBurger))
    PayTax=( (costofFries + costofDrinks + costofPizza + costofChickBurger + costofCheeseBurger + costofBurger)*0.18)
    TotalCost= (costofFries + costofDrinks + costofPizza + costofChickBurger + costofCheeseBurger + costofBurger)
    Ser_Charge= ((costofFries + costofDrinks + costofPizza + costofChickBurger + costofCheeseBurger + costofBurger)/100)
    Service=str('%.2f' % Ser_Charge )
    OverAllCost=str('%.2f' % (PayTax +  TotalCost +  Ser_Charge))
    PaidTax=str('%.2f' % PayTax)

    Service_charges.set(Service)
    cost.set(CostofMeal)
    tax.set(PaidTax)
    Sub_total.set(CostofMeal)
    Total.set(OverAllCost)

def quit():
    root.destroy()
def reset():
    ramd.set("")
    Fries.set("")
    Burger.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")
    Pizza.set("")
    Total.set("")
    Sub_total.set("")
    Service_charges.set("")
    Drinks.set("")
    tax.set("")
    cost.set("")


root.title("MY Restaurant")
root.geometry("1600x800+0+0")

textinput=StringVar()
operator=""

f=Frame(root,width=1600,height=50,relief=SUNKEN)
f.pack(side=TOP)

f1=Frame(root,width=1000,height=900,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=700,height=900,bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

l1=Label(f,font="arial 50 bold",text="Restaurant Management System",fg="red",bd=10,anchor="w")
l1.grid(row=0,column=0)

l1=Label(f,font="arial 30 bold",text=localtime,fg="red",bd=10,anchor="w")
l1.grid(row=1,column=0)


dis=Entry(f2,font="arial 25 bold",textvariable=textinput,bd=25,insertwidth=4,bg="powder blue", justify="right")
dis.grid(columnspan=4)

Button(f2,font="arial 25 bold",padx=16,pady=16,text="7",bg="powder blue",command=lambda:btnclick(7)).grid(row=2,column=0)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="8",bg="powder blue",command=lambda:btnclick(8)).grid(row=2,column=1)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="9",bg="powder blue",command=lambda:btnclick(9)).grid(row=2,column=2)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=2,column=3)


Button(f2,font="arial 25 bold",padx=16,pady=16,text="4",bg="powder blue",command=lambda:btnclick(4)).grid(row=3,column=0)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="5",bg="powder blue",command=lambda:btnclick(5)).grid(row=3,column=1)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="6",bg="powder blue",command=lambda:btnclick(6)).grid(row=3,column=2)
Button(f2,font="arial 25 bold",padx=17,pady=16,text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=3,column=3)


Button(f2,font="arial 25 bold",padx=16,pady=16,text="1",bg="powder blue",command=lambda:btnclick(1)).grid(row=4,column=0)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="2",bg="powder blue",command=lambda:btnclick(2)).grid(row=4,column=1)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="3",bg="powder blue",command=lambda:btnclick(3)).grid(row=4,column=2)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="*",bg="powder blue",command=lambda:btnclick("*")).grid(row=4,column=3)


Button(f2,font="arial 25 bold",padx=17,pady=16,text="c",bg="powder blue",command=btnclrardisplay).grid(row=5,column=0)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="0",bg="powder blue",command=lambda:btnclick(0)).grid(row=5,column=1)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="=",bg="powder blue",command=btnEqual).grid(row=5,column=2)
Button(f2,font="arial 25 bold",padx=16,pady=16,text="/",bg="powder blue",command=lambda:btnclick("/")).grid(row=5,column=3)


ramd=StringVar()
Fries=StringVar()
Burger=StringVar()
Chicken_Burger=StringVar()
Cheese_Burger=StringVar()
Pizza=StringVar()
Total=StringVar()
Sub_total=StringVar()
Service_charges=StringVar()
Drinks=StringVar()
tax=StringVar()
cost=StringVar()


l4=Label(f1,font="arial 19 bold",text="       Reference",bd=16,anchor="w")
l4.grid(row=0,column=0)
t4=Entry(f1,font="arial 20 bold",textvariable=ramd,bd=10,insertwidth=4,bg="powder blue",justify="right")
t4.grid(row=0,column=1)

l5=Label(f1,font="arial 19 bold",text="     Large Fries",bd=16,anchor="w")
l5.grid(row=1,column=0)
t5=Entry(f1,font="arial 20 bold",textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify="right")
t5.grid(row=1,column=1)

l6=Label(f1,font="arial 20 bold",text="   Burger Meal",bd=16,anchor="w")
l6.grid(row=2,column=0)
t6=Entry(f1,font="arial 20 bold",textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify="right")
t6.grid(row=2,column=1)

l7=Label(f1,font="arial 20 bold",text=" Chicken Meal",bd=16,anchor="w")
l7.grid(row=3,column=0)
t7=Entry(f1,font="arial 20 bold",textvariable=Chicken_Burger,bd=10,insertwidth=4,bg="powder blue",justify="right")
t7.grid(row=3,column=1)

l8=Label(f1,font="arial 20 bold",text="  Cheese Meal",bd=16,anchor="w")
l8.grid(row=4,column=0)
t8=Entry(f1,font="arial 20 bold",textvariable=Cheese_Burger,bd=10,insertwidth=4,bg="powder blue",justify="right")
t8.grid(row=4,column=1)

l9=Label(f1,font="arial 19 bold",text="   Pizza_Food",bd=20,anchor="w")
l9.grid(row=5,column=0)
t9=Entry(f1,font="arial 20 bold",textvariable=Pizza,bd=10,insertwidth=4,bg="powder blue",justify="right")
t9.grid(row=5,column=1)


l10=Label(f1,font="arial 19 bold",text="      Drinks",bd=16,anchor="w")
l10.grid(row=0,column=2)
t10=Entry(f1,font="arial 20 bold",textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify="right")
t10.grid(row=0,column=3)

l11=Label(f1,font="arial 19 bold",text="     Cost of Meal",bd=16,anchor="w")
l11.grid(row=1,column=2)
t11=Entry(f1,font="arial 20 bold",textvariable=cost,bd=10,insertwidth=4,bg="powder blue",justify="right")
t11.grid(row=1,column=3)

l12=Label(f1,font="arial 20 bold",text="   Service Charges",bd=16,anchor="w")
l12.grid(row=2,column=2)
t12=Entry(f1,font="arial 20 bold",textvariable=Service_charges,bd=10,insertwidth=4,bg="powder blue",justify="right")
t12.grid(row=2,column=3)

l13=Label(f1,font="arial 20 bold",text=" State Tax(GST)",bd=16,anchor="w")
l13.grid(row=3,column=2)
t13=Entry(f1,font="arial 20 bold",textvariable=tax,bd=10,insertwidth=4,bg="powder blue",justify="right")
t13.grid(row=3,column=3)

l14=Label(f1,font="arial 20 bold",text="  Sub Total",bd=16,anchor="w")
l14.grid(row=4,column=2)
t14=Entry(f1,font="arial 20 bold",textvariable=Sub_total,bd=10,insertwidth=4,bg="powder blue",justify="right")
t14.grid(row=4,column=3)

l15=Label(f1,font="arial 20 bold",text="   Total Cost",bd=20,anchor="w")
l15.grid(row=5,column=2)
t15=Entry(f1,font="arial 20 bold",textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify="right")
t15.grid(row=5,column=3)


Button(f1,padx=16,pady=8,bd=16,font="arial 20 bold",width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)
Button(f1,padx=16,pady=8,bd=16,font="arial 20 bold",width=10,text="Reset",bg="powder blue",command=reset).grid(row=7,column=2)
Button(f1,padx=16,pady=8,bd=16,font="arial 20 bold",width=10,text="Exit",bg="powder blue",command=quit).grid(row=7,column=3)







root.mainloop()