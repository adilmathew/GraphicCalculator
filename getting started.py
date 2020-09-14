from tkinter import *
window=Tk()
window.geometry("300x300")
#providing the dimension of the window
window.title("graphic calculator")
label=Label(window,text="making calculator",fg='blue',bg='yellow',relief="solid",font=("arial",16,"bold"))

#in Label we have pass window on which we want to perform these opeations
label.place(x=100,y=100)
#placing label with help of x y coordinate with place function

#mainloop should be at the end after adding all functionality
button1=Button(window,text="save",fg='black',bg='yellow',relief=GROOVE,font=("arial",10,"bold"))
button1.place(x=10,y=50)

def quitting():
    exit()
#we are making a function that will execute with command function when quit button is clicked
button2=Button(window,text="quit",fg='black',bg='yellow',relief="solid",font=("arial",10,"bold"),command=quitting)
button2.place(x=10,y=100)
menu=Menu(window)
window.config(menu=menu)
sub1=Menu(menu)
sub2=Menu(menu)
sub1.add_cascade(label="quit")
#sub2.add_command(label="save")

#we are creating an menu bar for adding save and quit there

window.mainloop()