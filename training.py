from tkinter import *
from tkinter import ttk, colorchooser
from PIL import Image,ImageDraw
import PIL
from PIL import ImageGrab
import win32gui
import io
import os
import csv

class main():
    def __init__(self, master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.width=200
        self.height=200
        self.old_x = None
        self.black = (0, 0, 0)
        self.white=(255,255,255)
        self.old_y = None
        self.s = ''
        self.path=" "
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>', self.paint)  # drwaing the line
        #self.linee=self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.i_train=0

    def paint(self, e):
         self.x1,self.y1=(e.x-1),(e.y-1)
         self.x2,self.y2=(e.x+1),(e.y+1)
         self.c.create_oval(self.x1,self.y1,self.x2,self.y2,fill="black",width=self.penwidth)
         self.draw.line([self.x1, self.y1, self.x2, self.y2], fill="black", width=self.penwidth)

    def reset(self,e):  # reseting or cleaning the canvas
        self.old_x = None
        self.old_y = None
    def changeW(self, e):  # change Width of pen through slider
        self.penwidth = e
    def clear(self):
        self.c.delete(ALL)
    def quitting(self):
        exit()
    def ans(self):
        eval(self.s)
    
    def New(self):
        self.i_train=0
        self.label=10
        self.path="Images/"+str(self.label)
        os.mkdir(self.path)


    def save(self):
        if(self.i_train==15):
            exit()
        
        else:
            HWND = self.c.winfo_id()
            rect = win32gui.GetWindowRect(HWND)
            ImageGrab.grab(rect).save(self.path+"/"+str(self.i_train)+".png")
            img_cv = Image.open(self.path+"/"+str(self.i_train)+".png")
            img_rgb = img_cv.convert("RGB")
            img_rgb=img_rgb.resize((50,50),PIL.Image.ANTIALIAS)
            img_rgb.save(self.path+"/"+str(self.i_train)+".png")
            img_bw=Image.open(self.path+"/"+str(self.i_train)+".png").convert("1")
            img_bw=img_bw.resize((28,28))
            data=[]
            data.append(int(self.label))
            for x in range(img_bw.width):
                for y in range(img_bw.height):
                    data.append(int(img_bw.getpixel((x,y))))
            
            with open('images.csv', "a", newline='') as csvfile: 
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerow(data) 
            

            self.i_train+=1
            self.clear()
        
        

    def change_fg(self):  # changing the pen color
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]
    def change_bg(self):  # changing the background color canvas
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def drawWidgets(self):
        self.controls = Frame(self.master,bg="black",padx=5,pady=5)
        self.controls.pack(side=LEFT)
        Button(self.controls,text="save",fg="black",command=self.save).grid(row=0,column=7)
        Button(self.controls,text="quit",fg="black",command=self.quitting).grid(row=1,column=7)
        Button(self.controls, text="clear", fg="black",command=self.clear).grid(row=2, column=7)
        Button(self.controls, text="ANS", fg="black", command=self.ans).grid(row=3, column=7)
        Button(self.controls, text="NEW", fg="black", command=self.New).grid(row=4, column=7)
        self.c = Canvas(self.master, width=self.width, height=self.height, bg=self.color_bg,highlightthickness=1, highlightbackground="green" )
        self.c.pack(side=BOTTOM, expand=True)
        self.image1=PIL.Image.new("RGB",(self.width,self.height),self.white)
        self.draw=ImageDraw.Draw(self.image1)


if __name__ == '__main__':
    root = Tk()
    main(root)
    #root.geometry("300x300")
    root.title('trainer')
    root.mainloop()
