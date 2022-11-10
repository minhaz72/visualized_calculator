# a simple calculator with python : 
# desine a simple calculator in tkinter : 
import tkinter 
from tkinter import * 
root= Tk()
root.title('calculator')
# entry ection : 
myentry=  Entry(root, width= 35 , font=  'Arial', borderwidth= 5 ).grid(row=0, column=0 , columnspan=3, padx=10 , pady=10 ) 

# button section 
# define a function  for number :  :  
def Btn1(number): 
    current_click=  myentry.get()
    myentry.delete(0, END)
    myentry.insert( 0, str(current_click) +  str(number ))
def clear(): 
    myentry.delete(0,  END)
# implement the arerthmatioc operation : 
def add_btn(): 
    first_click=myentry.get()    
    global first_number
    global math 
    math= 'addition '
    first_number= int(first_click) 
    myentry.delete(0, END )

def  sub_btn(): 
    first_click=myentry.get()    
    global first_number
    global math 
    math= 'substraction '
    first_number= int(first_click) 
    myentry.delete(0, END )


def mul_btn() :
    first_click=myentry.get()    
    global first_number
    global math 
    math= 'multipication '
    first_number= int(first_click) 
    myentry.delete(0, END )


def div_btn(): 
    first_click=myentry.get()    
    global first_number
    global math 
    math= 'division '
    first_number= int(first_click) 
    myentry.delete(0, END )


def equal_btn(): 
    secound_number=myentry.get()
    myentry.delete(0, END)
    if math== 'addition': 
        
        myentry.insert(0, int(first_number ) + int(secound_number ))
    elif math== 'substraction': 
        myentry.insert(0, int(first_number ) - int(secound_number ))
    elif math== 'multipication': 
        myentry.insert(0, int(first_number ) *  int(secound_number ))
    elif  math== 'division': 
        myentry.insert(0, int(first_number ) / int(secound_number ))
        
btn1=Button(root, text='1', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(1)).grid(row= 2, column=2)
btn2=Button(root, text='2', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(2)).grid(row= 2, column=3 )
btn3=Button(root, text='3', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(3)).grid(row= 2, column=4 )
btn4=Button(root, text='4', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(4)).grid(row= 3, column=1 )
btn5=Button(root, text='5', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(5)).grid(row= 3, column=2 )
btn6=Button(root, text='6', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(6)).grid(row= 3, column=3 )
btn7=Button(root, text='7', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(7)).grid(row= 3, column=4)
btn8=Button(root, text='8', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(8)).grid(row= 4, column=1 )
btn9=Button(root, text='9', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(9)).grid(row= 4, column=2 )
btn0=Button(root, text='0', font='Arial', padx=40, pady= 20 , command= lambda:Btn1(0)).grid(row= 4, column=3 )
btn_add=Button(root, text='+', font='Arial', padx=91, pady= 20 , command= add_btn, bg='yellow').grid(row= 4, column=4 )
btn_sub=Button(root, text='-', font='Arial', padx=40, pady= 20 , command=sub_btn).grid(row= 5, column=1 )
btn_mul=Button(root, text='x', font='Arial', padx=40, pady= 20 , command= mul_btn).grid(row= 5, column=2 )
btn_div=Button(root, text='/', font='Arial', padx=40, pady= 20 , command= div_btn).grid(row= 5, column=3 )
btn_clear=Button(root, text='clear', font='Arial', padx=40, pady= 20 ,command=clear).grid(row= 5, column=4 )
btn_equal=Button(root, text='=', font='Arial', padx=40, pady= 20 , command= equal_btn).grid(row= 6, column=1 )




root.mainloop()
