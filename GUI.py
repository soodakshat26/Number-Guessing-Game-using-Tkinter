from tkinter import*
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import  messagebox
import random



attempts=5
def checker():
    global attempts
    global score

    # attempts is decreased by 1 to reflect users remaining attempts.
    attempts -= 1

    # Getting users input and converting it to integer data type.
    guess = int(box.get())

    # Comparing guess to answer
    if n == guess:
        text.set("You win!!")
        check_button.pack_forget()
        score=20*(attempts+1)
        print(score)
        meter = tb.Meter(new_window,metersize=100,padding=5,amountused=score,subtext="SCORE")
        meter.pack()
        label5 = tb.Label(new_window, text="Your score is:"+str(score)+"/100", font=("Helvetica",20))
        label5.pack(padx=20, pady=20)

    # Ensuring the user still has attempts - if not remove option for more attempts.
    elif attempts == 0:
        text.set("You are out of attempts goodbye!")
        check_button.pack_forget()
    # If guess is less than the answer - update user with remaining attempts and tell them to enter a higher number.
    elif guess < n:
        text.set("Incorrect! - You have " + str(attempts) + " remaining attempts - Go higher!")
        # Clearing the input box for next attempt.
        box.delete(0, END)
    # If guess is higher than the answer - update user with remaining attempts and tell them to enter a lower number.
    elif guess > n:
        text.set("Incorrect! - You have " + str(attempts) + " remaining - Go lower!")
        # Clearing the input box for next attempt.
        box.delete(0, END)
    return

      
      
    
      
      
   






def clicker():
      global n
      l3=tb.Label(new_window,text=f'You get:')
      l3.pack()
      l3.config(text=" ")
      l3.config(text=f'Your Updated Level is {val_setting.get()}')
      
      if(val_setting.get()=="Easy"):
        label = tb.Label(new_window, text="Guess a Number between 1-10", font=("Helvetica",20))
        label.pack(padx=20, pady=20)
        n=random.randint(1,11)
      elif(val_setting.get()=="Medium"):
        label = tb.Label(new_window, text="Guess a Number between 1-50", font=("Helvetica",20))
        label.pack(padx=20, pady=20)
        n=random.randint(1,51)
      elif(val_setting.get()=="Hard"):
        label = tb.Label(new_window, text="Guess a Number between 1-100", font=("Helvetica",20))
        label.pack(padx=20, pady=20)
        n=random.randint(1,101)

      if (val_setting!="PY_VAR0"):
         global box
         box=tb.Entry(new_window,bootstyle='light',font="Helvetica",width=40)
         box.pack(pady=10)

      global check_button

      check_button=tb.Button(new_window,text="CHECK",command=checker)
      check_button.pack()
      global text
      text = StringVar()
      text.set("You have 5 attempts! Good luck")
      guess_attempts = Label(new_window, textvariable=text)
      guess_attempts.pack()











def open_new_play_page():
    # Create a new window for the new page
    global new_window
    new_window = tb.Toplevel(top)
    new_window.geometry("800x500")
    
    # Customize the new window as needed
    new_window.title("New Page")
    
    # Add widgets (labels, buttons, etc.) to the new window
   
    settings=['Easy','Medium','Hard']

    global val_setting
   
    val_setting=StringVar()
    for i in settings:
        # my_style=tb.Style()
        # my_style.configure('success.Outline.TButton',font=("Helvetica",15),bootstyle="success,Outline")
        tb.Radiobutton(new_window,bootstyle="danger",variable=val_setting,text=i,value=i).pack(pady=5)
    # l3=tb.Label(new_window,text=f'You get:')
    # l3.pack()
    # l3.config(new_window,text=f'You get:{val_setting.get()}')
    
    apply_button=tb.Button(new_window,text="APPLY",command=clicker)
   
   
    apply_button.pack()
    

    
    








def open_new_rules_page():
    # Create a new window for the new page
    new_window2 = tb.Toplevel(top)
    new_window2.geometry("1400x300")
    
    # Customize the new window as needed
    new_window2.title("New Page")
    
    # Add widgets (labels, buttons, etc.) to the new window
    label8 = tb.Label(new_window2, text="There are three levels to choose from: Easy, Medium and Hard", font=("Helvetica",20))
    label8.pack(padx=20, pady=6)
    label9 = tb.Label(new_window2, text="In easy level, you will have to guess a number from range 1-10", font=("Helvetica",20))
    label9.pack(padx=20, pady=6)
    label7 = tb.Label(new_window2, text="In medium level, you will have to guess a number from range 1-50 ", font=("Helvetica",20))
    label7.pack(padx=20, pady=6)
    label6 = tb.Label(new_window2, text="In hard level, you will have to guess a number from range 1-100", font=("Helvetica",20))
    label6.pack(padx=20, pady=6)
    label5 = tb.Label(new_window2, text="You will have a total of 5 attempts and will be scored based on the number of attempts taken", font=("Helvetica",20))
    label5.pack(padx=20, pady=6)

    










   






    
    















top= tb.Window(themename="superhero")
top.geometry("800x500")
fname=PhotoImage(file="C:/Users/Akshat Sood\OneDrive - rdmlpdpvt/Desktop/bg1.png")
bg_label=Label(top, image=fname)

head_label=Label(top,text="NUMGuessr",font=("Helvetica",70))



bg_label.place(x=0,y=0,relwidth=1,relheight=1)
head_label.pack(pady=30)
my_style=tb.Style()
my_style.configure('success.Outline.TButton',font=("Helvetica",30),bootstyle="success,Outline")
play_button=tb.Button(text="PLAY",bootstyle="info,outline",style="success.Outline.TButton",command=open_new_play_page)
play_button.pack(pady=5)
my_style2=tb.Style()
my_style2.configure('info.Outline.TButton',font=("Helvetica",30),bootstyle="success,Outline")
rule_button=tb.Button(text="RULES",bootstyle="info,outline",style="info.Outline.TButton",command=open_new_rules_page)
rule_button.pack(pady=20)
my_style2=tb.Style()
my_style2.configure('danger.Outline.TButton',font=("Helvetica",30),bootstyle="success,Outline")


# settings=['Easy','Medium','Hard']
# val_setting=StringVar()
# for i in settings:
#     tb.Radiobutton(,bootstyle="danger",variable=val_setting,text=i,value=i).pack(pady=20)

top.mainloop()